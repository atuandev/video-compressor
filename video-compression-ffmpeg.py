import os
from ffmpeg_progress_yield import FfmpegProgress

PREFIX_COMPRESSED_VIDEO = 'compressed_'

def compress_video(input_directory, output_directory, input_formats, output_format):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Get input formats. Default: mp4,mkv,avi
    input_formats = input_formats.split(',')

    # Process each file in the input directory
    for filename in os.listdir(input_directory):
        if any(filename.endswith(fmt.strip()) for fmt in input_formats):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, f'{PREFIX_COMPRESSED_VIDEO}{os.path.splitext(filename)[0]}.{output_format}')
            
            print(f"\nProcessing: {filename}")
            
            # Start compression with progress monitoring
            cmd = [
                'ffmpeg',
                '-y',
                '-i', input_path,
                '-c:v', 'libx264',
                '-c:a', 'copy',
                '-crf', '23',
                output_path
            ]
            ff = FfmpegProgress(cmd)
            
            # Create progress bar
            for progress in ff.run_command_with_progress():
                print(f"{progress:.2f}%")

            # Show compression info 
            original_size = os.path.getsize(input_path)
            compressed_size = os.path.getsize(output_path)
            show_compression_info(original_size, compressed_size)

def show_compression_info(original_size, compressed_size):
    # Tính phần trăm đã nén
    compression_ratio = (1 - compressed_size/original_size) * 100
    
    # Chuyển đổi kích thước sang đơn vị dễ đọc (KB, MB, GB)
    def convert_size(size_bytes):
        units = ['B', 'KB', 'MB', 'GB']
        index = 0
        while size_bytes >= 1024 and index < len(units) - 1:
            size_bytes /= 1024
            index += 1
        return f"{size_bytes:.2f} {units[index]}"

    # Hiển thị thông tin
    print(f"Kích thước gốc: {convert_size(original_size)}")
    print(f"Kích thước đã nén: {convert_size(compressed_size)}")
    print(f"Tỷ lệ nén: {compression_ratio:.1f}%")

def main():
    input_directory = input("Nhập đường dẫn thư mục chứa video: ").strip()
    output_directory = input("Nhập đường dẫn thư mục xuất video: ").strip()
    input_formats = input("Nhập định dạng video đầu vào (ví dụ: mp4,mkv,mov) [mặc định: mp4,mkv,mov]: ").strip() or "mp4,mkv,mov"
    output_format = "mp4"  # Fixed output format

    compress_video(input_directory, output_directory, input_formats, output_format)

if __name__ == "__main__":
    main()