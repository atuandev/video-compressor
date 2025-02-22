# Python Compress Video
Project này sẽ giúp giảm dung lượng của video nhanh chóng, miễn phí.

## Hướng dẫn setup:
##### 1. Clone `git clone git@github.com:atuandev/video-compressor.git`

##### 2. Setup Python Project để chạy được source này tại [đây](https://fork-eggnog-80b.notion.site/Setup-project-19c0e5ada1dd809096d2dfacc458115a)

##### 3. Tải phần mềm `ffmpeg`

- **Window**

Tải choco `winget install --id chocolatey.chocolatey --source winget`

Sử dụng: `choco install ffmpeg`

> Nếu lỗi lệnh choco, mở lại terminal với quyền admin

- **MacOS**

Sử dụng: `brew install ffmpeg`

- **Linux**

Sử dụng: `sudo apt install ffmpeg`

##### 4. Kiểm tra cài đặt

Sau khi cài đặt, mở Terminal/Command Prompt và gõ: `ffmpeg -version`

Nếu hiện thông tin phiên bản FFmpeg, việc cài đặt đã thành công.

##### 5. Chạy dự án

Kích hoạt môi trường ảo và gõ: `python .\video-compression-ffmpeg.py`
