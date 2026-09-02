---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-16
title: Hypium自动化测试如何访问设备的图库
breadcrumb: FAQ > DevEco Studio > 应用测试 > Hypium自动化测试如何访问设备的图库
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:add72f2911d3f9601543e5d7b0b06d3376701357a662a7e2ba46893313bba770
---

## 问题现象

如何使用Hypium库实现访问图库？

## 背景知识

* [照片和视频存储位置](faqs-local-file-manager-34.md)为/storage/cloud/100/files/Photo和/storage/media/100/local/files/Photo。
* mediatool是一个轻量级的命令行工具集合，开发者可通过此工具操作媒体库资源。媒体库为图库提供和管理数据，媒体库中的图片和视频会在图库界面呈现。具体请参考[mediatool工具使用指导](../harmonyos-guides/mediatool.md)。

## 解决方案

使用Hypium库实现访问图库，由于系统权限限制需要结合mediatool工具使用。最终可以实现访问图库。

* 查询图库/storage/media/100/local/files/Photo中目录以及文件。

  ```py
  import logging
  from devicetest.core.test_case import TestCase, Step
  from hypium import UiDriver

  class TC_001(TestCase):
      def __init__(self, configs):
          self.TAG = self.__class__.__name__
          super().__init__(self.TAG, configs)
          self.driver = UiDriver(self.device1)
          self.driver_width, self.driver_height = self.driver.get_display_size()

      def setup(self):
          Step('1.回到桌面')
          self.driver.swipe_to_home()

      def process(self):
          Step("步骤1：查询出/storage/media/100/local/files/Photo目录下文件夹")
          echo = self.driver.shell('mediatool ls -l /storage/media/100/local/files/Photo')
          file_list = echo.split('\n')[:-1]
          file_name = []
          for i in range(len(file_list) - 1):
              file_name_list = file_list[i].split()
              file_name.append(file_name_list[len(file_name_list) - 1])
          Step("步骤2：选择其中一个文件夹查看文件")
          file = self.driver.shell('mediatool ls -l /storage/media/100/local/files/Photo/{}'.format(file_name[0]))
          logging.info('file:' + str(file))

      def teardown(self):
          Step("收尾工作xxxx")
          pass
  ```
* 已知图片名称查看图片在设备中的位置，此处的文件名为图片设备显示名称display-name，可参考[mediatool查询命令](../harmonyos-guides/mediatool.md#查询命令mediatool-query)。

  ```py
  locations = self.driver.shell('mediatool query IMG_XXXXX_XXXXX.jpg')
  logging.info('locations:' + locations)
  ```
