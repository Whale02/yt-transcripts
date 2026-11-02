# Last Days 新视频抓取状态 — 2026-11-02

2026-11-02 已执行仓库现有的字幕采集和标准化入口，并尝试第二条公开字幕接口。两个视频在 YouTube 频道的相应播放列表中被确认，但 GitHub Actions 的出口 IP 遭 YouTube 屏蔽；以下均**未获得原始字幕**，未生成真实章节摘要或预言 claims。不可把这份状态文档当作内容提取结果。

| 来源 | 视频 ID | 视频 | 状态 |
|---|---|---|---|
| `@lastdays247/videos` 最新 | `URyAOyKCTdc` | https://www.youtube.com/watch?v=URyAOyKCTdc | 待取得字幕：YouTube 机器人验证 |
| `@lastdays247/streams` 最新 | `W7v5YD2SAn8` | https://www.youtube.com/watch?v=W7v5YD2SAn8 | 待取得字幕：YouTube 机器人验证 |

## 实际运行证据

- 初次抓取： https://github.com/Whale02/yt-transcripts/actions/runs/41414012488 （原脚本曾误报成功，实际新增字幕 0）。
- 修复状态检测后： https://github.com/Whale02/yt-transcripts/actions/runs/41414363903 （正确显示 failure）。
- 独立字幕接口尝试： https://github.com/Whale02/yt-transcripts/actions/runs/41414522969 （两个视频均 RequestBlocked，新增字幕 0）。

## 恢复方法

通过已授权、可访问这些视频字幕的服务读取完整带时间戳 transcript，或者提供本人能够使用的字幕文件。按仓库原有流程进入 `corpus` 或 `corpus-streams`，保持视频 ID、真实上传日期和每行时间戳；随后触发 `.github/workflows/section-all-transcripts.yml`，生成章节导航与 Key Points。针对明确、可检验的预言，还应单独按 `EXTRACT-GOAL.md` 提取时间、地点、具体结果、前瞻性证伪标准，并将其与事实核验严格分开。

**注意**：不得用推测补全字幕，也不得标记为已完成。
