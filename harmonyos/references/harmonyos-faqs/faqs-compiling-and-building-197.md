---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-197
title: 预览器触发构建，编译时发生daemon相关报错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 预览器触发构建，编译时发生daemon相关报错
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:33+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:3931c1459abd28fa020a580f27aeb5ca270f14bc035d202950a897492a5334b4
---

**问题现象**

IDE环境下，通过预览器间接调用hvigor执行构建，出现以下这几种报错:

```json5
hvigor ERROR: hvigor client: Connection between client and daemon is disconnected with a connect error
```

```screen
hvigor Create hvigor server failed. No Idle daemon can be found.
```

```screen
hvigor Create hvigor server failed. The daemon is closed or not the hvigor process.
```

```screen
长时间卡住在 hvigor client: Starting hvigor daemon.
```

**问题原因：**

1. hvigor尝试申请的端口范围(45000-45099)，所有端口都被占用或无权限
2. daemon进程被安全软件拦截，例如公司安全软件、VPN、流量代理、杀毒软件
3. hvigor没有用户目录下缓存路径的访问权限，或缓存文件损坏

**说明** 

预览器的运行强制要求hvigor运行在daemon模式下，因此所有关闭daemon的配置在执行预览构建时均不会生效。

**解决方案**

1. 检查确保端口(45000-45099)可用，检查本机路径访问权限可用，测试：

   ```bash
   netstat -ano | findstr 450
   ```

   ```bash
   ping 127.0.0.1
   ```
2. 检查并关闭可能会拦截的安全软件
3. 删除以下缓存目录：
   1. Windows: C:\Users\<用户名>\.hvigor
   2. Linux/macOS: ~/.hvigor
4. 如果以上方式仍然报错，卸载现有 DevEco Studio并执行默认安装后，重新创建项目后尝试预览
