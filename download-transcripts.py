#!/usr/bin/env python3
"""
下载 Elon Musk 访谈视频的字幕脚本
"""

import re
import subprocess
import sys
import time
from pathlib import Path

def extract_youtube_links(markdown_file):
    """从 markdown 文件中提取 YouTube 链接"""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配格式: - YYYY-MM-DD: [标题](YouTube链接)
    pattern = r'- (\d{4}-\d{2}-\d{2}):\s+\[([^\]]+)\]\((https://www\.youtube\.com/watch\?v=([a-zA-Z0-9_-]+))\)'
    matches = re.findall(pattern, content)
    
    return [
        {
            'date': match[0],
            'title': match[1],
            'url': match[2],
            'video_id': match[3]
        }
        for match in matches
    ]

def download_subtitle(video_info, output_dir='transcripts'):
    """下载单个视频的字幕"""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # 构建输出文件名
    date = video_info['date']
    title = video_info['title']
    video_id = video_info['video_id']
    url = video_info['url']
    
    # 清理标题中的特殊字符
    safe_title = re.sub(r'[^\w\s-]', '', title)
    safe_title = re.sub(r'[-\s]+', '-', safe_title)
    
    output_template = f"{date}-{safe_title}"
    
    cmd = [
        'yt-dlp',
        '--write-auto-sub',          # 下载自动生成的字幕
        '--sub-lang', 'en',           # 英文字幕
        '--skip-download',            # 只下载字幕，不下载视频
        '--convert-subs', 'srt',      # 转换为 SRT 格式
        '--output', str(output_path / output_template),
        url
    ]
    
    print(f"\n{'='*60}")
    print(f"日期: {date}")
    print(f"标题: {title}")
    print(f"视频ID: {video_id}")
    print(f"URL: {url}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            print(f"✅ 字幕下载成功")
            return True
        else:
            print(f"❌ 下载失败: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"⏱️ 超时")
        return False
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

def main():
    markdown_file = 'references/cheat-sheets-elon-musk-full.md'
    
    print("="*60)
    print("Elon Musk 访谈字幕下载器")
    print("="*60)
    
    # 提取所有 YouTube 链接
    videos = extract_youtube_links(markdown_file)
    print(f"\n找到 {len(videos)} 个 YouTube 视频")
    
    # 检查已下载的字幕
    existing = list(Path('transcripts').glob('*.srt'))
    print(f"已有 {len(existing)} 个字幕文件")
    
    # 询问用户要下载多少个
    print(f"\n选项:")
    print(f"  1. 下载全部 ({len(videos)} 个)")
    print(f"  2. 下载前10个")
    print(f"  3. 下载前20个")
    print(f"  4. 退出")
    
    choice = input("\n请选择 (1-4): ").strip()
    
    if choice == '4':
        print("退出")
        return
    
    limit = len(videos) if choice == '1' else 10 if choice == '2' else 20 if choice == '3' else 0
    
    if limit == 0:
        print("无效选择")
        return
    
    videos_to_download = videos[:limit]
    
    print(f"\n开始下载 {len(videos_to_download)} 个字幕...")
    
    success_count = 0
    fail_count = 0
    
    for i, video in enumerate(videos_to_download, 1):
        print(f"\n[{i}/{len(videos_to_download)}]")
        
        if download_subtitle(video):
            success_count += 1
        else:
            fail_count += 1
        
        # 避免请求过快
        if i < len(videos_to_download):
            time.sleep(2)
    
    print(f"\n{'='*60}")
    print(f"下载完成！")
    print(f"成功: {success_count} 个")
    print(f"失败: {fail_count} 个")
    print(f"文件保存在: transcripts/ 目录")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
