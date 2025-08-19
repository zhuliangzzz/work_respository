#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo6.py
   @author:zl
   @time: 2025/8/18 10:07
   @software:PyCharm
   @desc:
"""
from PIL import Image, ImageOps

# position = (100, 50)


def merge_images_with_cutout(subject_path, background_path, output_path):
    # 打开图片并确保都是RGBA模式（带透明度）
    subject = Image.open(subject_path).convert("RGBA")
    background = Image.open(background_path).convert("RGBA")

    # 确保两张图片尺寸相同
    if subject.size != background.size:
        background = background.resize(subject.size)

    # 获取主体图的alpha通道（透明度通道）
    subject_alpha = subject.split()[3]

    # 创建一个与背景图相同大小的透明图层
    cutout_background = Image.new("RGBA", background.size, (0, 0, 0, 0))

    # 将背景图粘贴到透明图层上，但只在主体图不透明的地方显示
    # 这里使用主体图的alpha通道的反相作为遮罩
    # 因为我们要"切掉"的是主体图的部分
    cutout_background.paste(background, (0, 0), ImageOps.invert(subject_alpha))

    # 合并两张图片（切掉背景后的背景图 + 主体图）
    result = Image.alpha_composite(cutout_background, subject)
    result.show()
    result.save(output_path)


# 使用示例
merge_images_with_cutout("images/bg.jpeg","images/demo.png",  "result.png")