# SteamTool 清单下载器

这是一个基于 Flask 和原生 JavaScript 构建的 Web 应用，用于浏览、搜索和生成 Steam 游戏下载链接。应用会从 Steam API 获取最新的游戏列表，并提供一个美观、响应式的界面进行交互。

<img width="2550" height="1288" alt="Image" src="https://github.com/user-attachments/assets/006f9766-1289-430a-bff4-15bd0565f643" />

## ✨ 主要功能

-   **实时游戏搜索**：按游戏名称或 AppID 快速筛选海量游戏。
-   **多种排序方式**：支持按名称 (A-Z)、AppID (新到旧 / 旧到新) 进行排序。
-   **动态分页浏览**：采用高效的前端分页，流畅浏览数万款游戏。
-   **一键复制 AppID**：方便地将游戏的 AppID 复制到剪贴板。
-   **生成下载链接**：点击 "下载" 按钮，直接跳转到对应的 ManifestHub ZIP 文件下载页面。
-   **本地缓存**：首次运行后，游戏列表会被缓存到本地 (`game_list_cache.json`)，加快后续启动速度。
-   **响应式设计**：界面在桌面和移动设备上均有良好表现。

## 🛠️ 技术栈

-   **后端**: Flask (Python)
-   **前端**: HTML, Tailwind CSS, 原生 JavaScript
-   **数据源**: Steam Web API

## 🚀 如何运行

请确保你的电脑上已经安装了 Python 3。

1.  **克隆仓库**
    ```bash
    git clone [https://github.com/name1oss/SteamTool-PurityDownload.git](https://github.com/name1oss/SteamTool-PurityDownload.git)
    cd SteamTool-PurityDownload
    ```

2.  **创建并激活虚拟环境 (推荐)**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **安装依赖**
    ```bash
    pip install -r requirements.txt
    ```

4.  **运行应用**
    ```bash
    python app.py
    ```

5.  **访问应用**
    应用启动后，它会自动在你的默认浏览器中打开 `http://127.0.0.1:5000/`。
    首次运行时，程序需要从 Steam API 获取游戏列表，请耐心等待片刻。

## 📝 注意事项

-   应用依赖的下载链接指向 `github.com/SteamAutoCracks/ManifestHub`。请确保该仓库的链接结构没有发生变化。
-   首次启动时获取 Steam 游戏列表可能需要一些时间，具体取决于你的网络状况。成功获取后，列表会缓存为 `game_list_cache.json` 以便快速启动。

## 📜 开源许可

本项目采用 [MIT License](LICENSE)。
