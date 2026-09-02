---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-48
title: USB设备调用libusb库读写fd时报错
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > USB设备调用libusb库读写fd时报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8a6598c5d5451b83f49fccb1aec9eeb22b3fb8d3af87875378e7af57d21da84e
---

## 问题现象

USB设备调用libusb库的ioctl函数进行设备读写时失败，返回错误码16，提示“文件已存在”或“资源已被占用”。

```screen
ioctl(hpriv - > fd, IOCTL_USBFS_SUBMITURB, urb); // 失败，errno=16
```

涉及到接口占用部分的问题代码示例参考如下：

* TS侧USB初始化。

  ```screen
  initUUBar(device: usbManager.USBDevice){
    if(this.usbPipe != null){
      return
    }
    this.initEndpoints(device)
    this.usbPipe = usbManager.connectDevice(device)
    usbManager.claimInterface(this.usbPipe,device.configs[0].interfaces[0])
    usbManager.setConfiguration(this.usbPipe,device.configs[0])
    usbManager.setInterface(this.usbPipe,device.configs[0].interfaces[0])
    this.usbPipeFd = usbManager.getFileDescriptor(this.usbPipe)
  }
  ```
* C++侧调用libusb库的ioctl函数进行设备读写。

  ```screen
  r = ioctl(hpriv->fd, IOCTL_USBFS_SUBMITURB, urb); // 这里返回错误码16
  if (r < 0) {
    free(urb);
    tpriv->urbs = NULL;
    if (errno == ENODEV)
      return LIBUSB_ERROR_NO_DEVICE;
    usbi_err(TRANSFER_CTX(transfer), "submiturb failed, errno=%d", errno); // 这里返回错误码16
    return LIBUSB_ERROR_IO;
  }
  ```

## 解决方案

使用usbManager的claimInterface方法时，系统会独占该接口。其他进程（包括使用libusb的进程）将无法再访问该接口。所以使用libusb场景，不要调用usbManager提供的claimInterface等接口，否则会造成USB服务进程占用接口，其他进程使用时会报错。

## 总结

使用libusb场景，不要调用usbManager提供的claimInterface等接口，否则会造成USB服务进程占用接口，其他进程使用时会报错。
