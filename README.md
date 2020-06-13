# thvl-download-videos
Tải phim từ trang thvli.vn

## Hướng dẫn sử dụng
- Cài đặt streamlink từ trang chủ, lựa chọn bản portable [https://streamlink.github.io/install.html#windows-portable-version](https://streamlink.github.io/install.html#windows-portable-version)
- Sao chép tập tin **thvl.py** vào thư **mục streamlink\plugins**
- Sao chép tập tin **playlist_download.py** vào thư mục gốc (thư mục có tập tin **streamlink.bat**)
- Mở cmd hoặc powershell và chạy lệnh sau:
	```
	.\python\python.exe playlist_download.py
	hoặc
	.\Python 3.6.3\python.exe playlist_download.py
	```
- Nếu bạn muốn tải về danh sách các phim thì nhập url phim mà bạn muốn tải về. Ví dụ:
	```
	".\Python 3.6.3\python.exe" playlist_download.py
	 URL: https://www.thvli.vn/detail/me-ghe/
	```
- Nếu bạn chỉ muốn tải 1 phim nào đó thì làm như sau. Ví dụ:
	```
	Streamlink.bat --ringbuffer-size=64M -o <tên video.ts> <url phim> best
	Streamlink.bat --ringbuffer-size=64M -o tap5.ts https://www.thvli.vn/detail/ngam-ngui/47891aec-0054-4469-9292-c238d94cbdd6 best
	```
	Với best là chất lượng video cao nhất.

### Hỗ trợ nền tảng
* [x] windows

