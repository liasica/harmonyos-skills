---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-75
title: hdc调试设备报错：hdc server port XXXX has been used，切换端口无效
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > hdc调试设备报错：hdc server port XXXX has been used，切换端口无效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:d24ef3b4450f37ee29e6e2209f621cad326d9c31b427ac0e0616708b81b4881e
---

**问题现象**

hdc调试设备提示报错：hdc server port XXXX has been used，手动切换端口无法解决。

**可能原因**

1. 端口占用。
2. 端口拦截。

**解决措施**

1. 端口占用请尝试以下方法：
   * 更换端口，通过配置环境变量OHOS\_HDC\_SERVER\_PORT配置可用端口如18710，配置完成后请重启命令行或重启使用到hdc的软件（如模拟器、DevEco Studio、DevEco系列、xdevice等软件）。
   * 查找占用端口的软件并解除占用。

     Windows系统：

     ```powershell
     查询端口
     $ netstat -ano | findstr :{端口号}
     停止服务
     $ taskkill /PID {PID号} /F
     注：实际使用时请替换为真实端口号和PID号
     ```

     Linux/MacOS系统：

     ```powershell
     查询端口
     $ lsof -i :{端口号}
     $ netstat -tuln | grep :{端口号}
     停止服务
     $ kill -9 {PID号}
     注：实际使用时请替换为真实端口号和PID号
     ```
   * Windows平台如果查询不到被占用的端口可尝试以下方法

     ```powershell
     查看动态端口范围
     $ netsh int ipv4 show dynamicport tcp
     查看例外端口范围
     $ netsh interface ipv4 show excludedportrange protocol=tcp
     ```

     如果查询列表中提示被占用的端口在例外端口范围中，执行以下步骤，或手动在任务管理器中重启Hyper-V服务

     ```powershell
     禁用Hyper-V [需要重启电脑]
     $ dism.exe /Online /Disable-Feature:Microsoft-Hyper-V
     启动Hyper-V [需要重启电脑]
     $ dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All
     ```
2. 端口拦截需检查本地是否开启相关防火墙拦截类软件，如果开启请调整相关安全组设置或关闭软件后重试。
