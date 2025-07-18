#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:main.py
   @author:zl
   @time: 2025/7/17 9:30
   @software:PyCharm
   @desc:
"""
import pyzipper
import os
from tqdm import tqdm  # 用于显示进度条


def encrypt_folder_with_aes(
        folder_path,
        output_zip,
        password,
        compression=pyzipper.ZIP_DEFLATED,
        encryption=pyzipper.WZ_AES
):
    """
    使用 AES 加密整个文件夹

    参数:
        folder_path: 要加密的文件夹路径
        output_zip: 输出的 ZIP 文件路径
        password: 加密密码
        compression: 压缩方法 (默认 DEFLATED)
        encryption: 加密方法 (默认 AES-256)
    """
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_zip) or '.', exist_ok=True)

    try:
        with pyzipper.AESZipFile(
                output_zip,
                'w',
                compression=compression,
                encryption=encryption
        ) as zipf:
            # 设置密码
            zipf.setpassword(password.encode('utf-8'))

            # 获取文件夹中所有文件
            file_paths = []
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_paths.append(os.path.join(root, file))

            # 添加文件到 ZIP (带进度条)
            for file in tqdm(file_paths, desc="加密文件中"):
                # 计算相对路径
                arcname = os.path.relpath(file, folder_path)
                zipf.write(file, arcname)

        print(f"\n 文件夹 '{folder_path}' 已成功加密为 '{output_zip}'")
        return True

    except Exception as e:
        print(f"\n 加密失败: {str(e)}")
        return False


def decrypt_aes_zip(
        zip_path,
        output_folder,
        password,
        overwrite=False
):
    """
    解密 AES 加密的 ZIP 文件

    参数:
        zip_path: 加密的 ZIP 文件路径
        output_folder: 解压目录
        password: 解密密码
        overwrite: 是否覆盖已存在文件
    """
    # 确保输出目录存在
    os.makedirs(output_folder, exist_ok=True)

    try:
        with pyzipper.AESZipFile(zip_path, 'r') as zipf:
            # 验证密码
            zipf.setpassword(password.encode('utf-8'))

            # 获取文件列表
            file_list = zipf.namelist()

            # 解压文件 (带进度条)
            for file in tqdm(file_list, desc="解密文件中"):
                # 检查文件是否已存在
                dest_path = os.path.join(output_folder, file)
                if os.path.exists(dest_path) and not overwrite:
                    raise FileExistsError(f"文件 '{file}' 已存在")

                # 解压文件
                zipf.extract(file, output_folder)

        print(f"\n 文件 '{zip_path}' 已成功解密到 '{output_folder}'")
        return True

    except Exception as e:
        print(f"\n 解密失败: {str(e)}")
        return False

# 示例用法
if __name__ == "__main__":
    # 加密示例
    folder_to_encrypt = "module"
    encrypted_zip = "protected_data.zip"
    password = "123456"

    print("开始加密文件夹...")
    encrypt_folder_with_aes(folder_to_encrypt, encrypted_zip, password)

    # 解密示例
    # print("\n开始解密文件...")
    # decryption_output = "decrypted_data"
    # decrypt_aes_zip(encrypted_zip, decryption_output, password)