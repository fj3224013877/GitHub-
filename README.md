# GitHub Trending Repositories

## 项目简介

本项目旨在定期爬取 GitHub 上某个编程语言的热门项目数据，并将这些数据推送到微信。通过使用 GitHub Actions 自动化工作流，用户可以每天定时获取最新的热门项目信息，并通过 Server酱将数据推送到个人微信。

## 功能特性

- **定时爬取**：使用 GitHub Actions 定时任务，每天定时爬取 GitHub 上指定编程语言的热门项目。
- **数据解析**：使用 BeautifulSoup 解析 GitHub 热门项目页面，提取项目名称、描述、星标数、Fork 数和项目 URL。
- **数据存储**：将爬取的数据保存到 CSV 文件中，便于后续分析和查看。
- **微信推送**：通过 Server酱将爬取到的热门项目数据推送到个人微信，用户可以随时查看最新的热门项目。

## 使用技术

- **编程语言**：Python
- **网页爬取**：requests, BeautifulSoup
- **数据处理**：pandas
- **自动化工作流**：GitHub Actions
- **消息推送**：Server酱

## 环境配置

1. **Python 环境**：确保已安装 Python 3.x 版本。
2. **依赖库**：安装所需的 Python 库。
   ```sh
   pip install requests beautifulsoup4 pandas
## 配置 GitHub Secrets

1. 打开你的 GitHub 仓库，点击 "Settings"。
2. 在左侧菜单中选择 "Secrets"。
3. 点击 "New repository secret" 按钮，添加两个新的 Secret：
   - `SCKEY`：值为你的 Server酱的 SCKEY。
   - `LANGUAGE`：值为你想要爬取的编程语言，例如 `python`、`java` 等。
