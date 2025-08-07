import shutil, os, time
from datetime import datetime

class BackupManager:
    def __init__(self, logger):
        self.logger = logger

    def generate_backup_name(self, base_name, version):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return f"{base_name}_{timestamp}_v{version}"

    def count_files(self, path):
        total_files = 0
        for root, dirs, files in os.walk(path):
            total_files += len(files)
        return total_files

    def backup_folder(self, src, dest, version, zip_backup=False):
        if not os.path.exists(src):
            self.logger.log("ERROR", f"Source path does not exist: {src}")
            return False

        name = self.generate_backup_name("backup", version)
        dest_path = os.path.join(dest, name)
        start_time = time.time()

        try:
            file_count = self.count_files(src)

            if zip_backup:
                shutil.make_archive(dest_path, 'zip', src)
            else:
                shutil.copytree(src, dest_path)

            duration = round(time.time() - start_time, 2)
            size_mb = self.calculate_directory_size_mb(dest_path if not zip_backup else dest_path + ".zip")

            self.logger.log("INFO", (
                f"Backup completed at '{dest_path}' | "
                f"Files: {file_count} | "
                f"Time: {duration}s | "
                f"Size: {size_mb} MB"
            ))
            return True

        except Exception as e:
            self.logger.log("ERROR", f"Backup failed: {e}")
            return False

    def calculate_directory_size_mb(self, path):
        total_size = 0
        if os.path.isfile(path):
            total_size = os.path.getsize(path)
        else:
            for dirpath, dirnames, filenames in os.walk(path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if os.path.exists(fp):
                        total_size += os.path.getsize(fp)
        return round(total_size / (1024 * 1024), 2)
