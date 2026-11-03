# Last Days 最新视频采集审计（更新于 2026-11-03）

> 本文件最初的“两个视频均未得到字幕”状态已经过时。2026-11-02 后续归档通过替代来源取得了两份带时间戳完整字幕，已完成章节和人工语义整理；**预言数据库仍需单独入库/复核，不等于命中率已核验**。

| 视频 ID | 对应内容 | 原始字幕 | 章节/内容 | 独立预言入库 |
|---|---|---|---|---|
| `W7v5YD2SAn8` | Come pray with me（YouTube 2026-11-02 UTC；美国西部时间 11-01 晚） | 已归档于 `corpus-streams/`，含 manifest | `exports/all-videos/W7v5YD2SAn8.md`、`exports/semantic/W7v5YD2SAn8.md` | `mentions-new-live-2026-11-02.json` 待正式 load/review/validate |
| `URyAOyKCTdc` | Palestinian muslim gets born again（YouTube 2026-10-31 UTC） | 已归档于 `corpus/`，含 manifest | `exports/all-videos/URyAOyKCTdc.md`、`exports/semantic/URyAOyKCTdc.md` | 访谈中的嘉宾观点须独立于 Brandon 的预言 |
| `OU3zNmq_QaY` | There is not enough urgency in the church（发现于 2026-11-02 公开转载；原始上传时间未核实） | **尚未归档/取得完整字幕** | 待处理 | 不得生成或计分断言 |

视频：https://www.youtube.com/watch?v=W7v5YD2SAn8 、https://www.youtube.com/watch?v=URyAOyKCTdc 、https://www.youtube.com/watch?v=OU3zNmq_QaY 。

## 来源和阶段

最初 GitHub Actions 两条获取途径遭 YouTube bot 检测：原始运行 [41414012488](https://github.com/Whale02/yt-transcripts/actions/runs/41414012488)、重试 [41414363903](https://github.com/Whale02/yt-transcripts/actions/runs/41414363903) 和替代公开字幕端点 [41414522969](https://github.com/Whale02/yt-transcripts/actions/runs/41414522969)。这三个运行未新增字幕。

但后续通过另一个字幕来源，视频 `W7v5YD2SAn8`、`URyAOyKCTdc` 的带时间戳原文已进入 GitHub。对应 `manifest.tsv` 和 `exports/all-videos/INDEX.md` 为证。不得再把旧运行失败当作截至今日的唯一结论。

2026-11-03 通过公开转载找到 `OU3zNmq_QaY`，见 https://www.bannedbook.org/bnews/zh-tw/sohnews/20261102/2376210.html 。转发日期不等于 YouTube 上传日期；尚未取得可复核字幕。Web 页面可用于发现 ID，不能代替带时间戳的讲话原文。

## 下一处理工序

1. **新增字幕**：分别检查 `@lastdays247/videos`、`streams`，经可用字幕来源取得标题、准确上传日、完整 timestamps，按原格式入 `corpus/` 或 `corpus-streams/`，并更新 manifest。
2. **章节**：运行 `scripts/section_all_transcripts.py`；保留全部原文，不将 speaking-in-tongues 自动误识文本当成有确定含义的词句。
3. **主张**：根据 `EXTRACT-GOAL.md` 将 Brandon 的异象、祈祷、嘉宾讲话、引用新闻、旧预言重复分别归类；逐个检验细节记录首述日、事件窗口和事前证伪标准。
4. **数据库**：只有原始视频先 `prophecy.py ingest` 后才可 `load`；`review` 后再 `validate`。同一预言不同讲述版本以 `delta_type` 标记，不能凭标题或讨论主题判断命中。
5. **选举评分**：2026-11-03 选举前不提前判定参众两院和佛州州长结果；结果可得后以近最终/官方结果评估，祷告“可能改变”另列、不改变实际观察。

**未完成项**：`OU3zNmq_QaY` 的原始字幕和上传日期；已提取的 2026-11-02 预言候选尚未确认写入 LFS 管理的 `prophecy.db`。记录为待办，不虚报完成。
