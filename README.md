# 考试宝 📝

离线考试软件，内容内置在 APK 中，不需要联网，打开即用。

---

## 🚀 构建 APK（二选一）

### 方式一：本地构建（需要 Node.js + Android Studio）

**一次性安装环境：**
1. 安装 [Node.js](https://nodejs.org)（LTS 版本）
2. 安装 [Android Studio](https://developer.android.com/studio)
3. 在 Android Studio 中：SDK Manager → 安装 Android 13+ SDK 和 Build Tools

**每次构建 APK：**
```bash
cd exam-app
npm install
npx cap add android
npx cap sync android
npx cap open android
```
然后在 Android Studio 中：**Build → Build Bundle(s) / APK(s) → Build APK(s)**

APK 位于 `android/app/build/outputs/apk/debug/app-debug.apk`

---

### 方式二：GitHub Actions 自动构建（推荐）

推送到 GitHub，自动构建 APK，无需本地安装 Android Studio。

1. 把 `exam-app` 推送到 GitHub 仓库
2. 在仓库 Settings → Actions → 启用
3. 每次推送自动构建，在 Actions 页面下载 APK

> GitHub Actions 工作流文件：`.github/workflows/build-apk.yml`

---

## 📝 题库格式

```json
{
  "name": "题库名称",
  "questions": [
    { "type": "single",    "question": "题目", "options": ["A","B"], "answer": 0 },
    { "type": "multiple",  "question": "题目", "options": ["A","B"], "answer": [0] },
    { "type": "truefalse", "question": "题目", "answer": true },
    { "type": "fill",      "question": "___填空", "answer": "答案" }
  ]
}
```

---

## 功能

- 题库导入（粘贴 JSON 或上传文件）
- 随机抽题，支持四种题型
- 考前登记：部门、姓名
- 即时评分，自动保存考试记录
- 导出 CSV 方便抄录
- 完全离线运行，无需网络
