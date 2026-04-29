---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-10
title: DevEco Studio AppAnalyzer-安装Python依赖错误
breadcrumb: FAQ > DevEco Studio > 应用测试 > DevEco Studio AppAnalyzer-安装Python依赖错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b2b4436c7e85759051697ee5a84e833c07a39e33f1219729557645d4ae2cfe05
---

**问题现象**

安装Python依赖报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/9SNxKQv6QISjTP9s9lZnXA/zh-cn_image_0000002265289721.png?HW-CC-KV=V1&HW-CC-Date=20260429T062136Z&HW-CC-Expire=86400&HW-CC-Sign=3D16390E737E3D101B1A36F038D76631A57F87D12489205D151BE84AFAD7F2F5)

**可能原因**一

pip配置问题。

**解决措施**

1. 修改pip配置。

   pip的配置文件位于用户根目录下的：~/.pip/pip.conf（Windows路径为：C:\Users\<UserName>\pip\pip.ini\*）。 开发者可以配置如下内容：

   ```
   1. [global]
   2. index-url = https://mirrors.huaweicloud.com/repository/pypi/simple
   3. trusted-host = mirrors.huaweicloud.com
   4. timeout = 120
   ```

   如需设置代理，可以参考以下配置，如果username、password包含特殊字符，需要进行转义。**proxyserver和port请按照实际代理服务器进行修改**。示例如下所示：

   ```
   1. [global]
   2. index-url = https://mirrors.huaweicloud.com/repository/pypi/simple
   3. proxy = http://username:password@proxyserver:port/
   4. trusted-host = mirrors.huaweicloud.com
   5. timeout = 120
   ```

   说明

   如果password中存在特殊字符，如@、#、\*等符号，可能导致配置不生效，建议将特殊字符替换为ASCII码，并在ASCII码前加百分号%。常用符号替换为ASCII码对照表如下：

   * !：%21
   * @：%40
   * #：%23
   * $：%24
   * &：%26
   * \*：%2A
2. 查看本地生效的pip配置。

   ```
   1. pip config list
   ```

**可能原因二**

Win系统卸载Python时有残留。

**解决措施**

Win系统卸载Python时未删除Python安装目录，需要清理Python的安装目录。

**可能原因三**

无外网访问权限。

**解决措施**

冷启动、白块检测、UX检测需要网络下载依赖。请更换有外网访问权限的网络。

**可能原因四**

paddlepaddle==2.6.1已经日落，导致pip安装失败

**解决措施**

MAC

```
1. //进入python安装目录
2. cd python_dir_xxxx
3. //python3.9安装命令
4. ./python -m pip install https://paddle-wheel.bj.bcebos.com/2.6.1/macos/macos-cpu-openblas/paddlepaddle-2.6.1-cp39-cp39-macosx_10_9_x86_64.whl
5. //python3.10安装命令
6. ./python -m pip install https://paddle-wheel.bj.bcebos.com/2.6.1/macos/macos-cpu-openblas/paddlepaddle-2.6.1-cp310-cp310-macosx_10_9_x86_64.whl
7. //python3.11安装命令
8. ./python -m pip install https://paddle-wheel.bj.bcebos.com/2.6.1/macos/macos-cpu-openblas/paddlepaddle-2.6.1-cp311-cp311-macosx_10_9_x86_64.whl
9. //python3.12安装命令
10. ./python -m pip install https://paddle-wheel.bj.bcebos.com/2.6.1/macos/macos-cpu-openblas/paddlepaddle-2.6.1-cp312-cp312-macosx_10_9_x86_64.whl
```

Win

```
1. //进入python安装目录
2. cd python_dir_xxxx
3. ./python.exe -m pip install paddlepaddle==2.6.1 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/
```

**可能原因五**

Python兼容性问题。

**解决措施**

Python与某些指定版本的依赖不兼容，支持的版本为**Python 3.9 ~3.12**，推荐**Python 3.11.7。**如果Python最新的版本与一些依赖不兼容，建议卸载Python并安装推荐版本或者更新[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 分类 | 三方库 | DevEco Studio 5.0.x | DevEco Studio 5.1.x | DevEco Studio 6.0.x |
| 冷启动&&白块检测 | Flask | 3.0.3 | 3.0.3 | 3.0.3 |
| 冷启动&&白块检测 | numpy | 1.26.4 | 1.26.4 | 1.26.4 |
| 冷启动&&白块检测 | onnxruntime | 1.19.2 | 1.19.2 | 1.19.2 |
| 冷启动&&白块检测 | opencv-python | 4.10.0.84 | 4.10.0.84 | 4.10.0.84 |
| 冷启动&&白块检测 | pillow | 10.4.0 | 10.4.0 | 10.4.0 |
| 冷启动&&白块检测 | pyclipper | 1.3.0.post6 | 1.3.0.post6 | 1.3.0.post6 |
| 冷启动&&白块检测 | shapely | 2.0.6 | 2.0.6 | 2.0.6 |
| 冷启动&&白块检测 | waitress | 3.0.2 | 3.0.2 | 3.0.2 |
| 冷启动-自动 | hypium | NA | 5.0.7.200 | 5.0.7.200 |
| 冷启动-自动 | xdevice | NA | 5.0.7.200 | 5.0.7.200 |
| 冷启动-自动 | xdevice-devicetest | NA | 5.0.7.200 | 5.0.7.200 |
| 冷启动-自动 | xdevice-ohos | NA | 5.0.7.200 | 5.0.7.200 |
| 冷启动-自动 | loguru | NA | 0.7.2 | 0.7.2 |
| 冷启动-自动 | numpy | NA | 1.26.4 | 1.26.4 |
| 冷启动-自动 | stable\_baselines3 | NA | 2.3.2 | 2.3.2 |
| 冷启动-自动 | gym | NA | 0.26.2 | 0.26.2 |
| 冷启动-自动 | gym-notices | NA | 0.0.8 | 0.0.8 |
| 冷启动-自动 | gymnasium | NA | 0.29.1 | 0.29.1 |
| 冷启动-自动 | Shimmy | NA | 1.3.0 | 1.3.0 |
| 冷启动-自动 | opencv-python | NA | 4.10.0.84 | 4.10.0.84 |
| 冷启动-自动 | cffi | NA | 1.17.1 | 1.17.1 |
| 冷启动-自动 | pynacl | NA | 1.5.0 | 1.5.0 |
| 冷启动-自动 | torch | NA | python版本<3.12：2.0.0 | python版本<3.12：2.0.0  python版本==3.12：2.2.0 |
| 冷启动-自动 | torchaudio | NA | python版本<3.12：2.0.0 | python版本<3.12：2.0.0  python版本==3.12：2.2.0 |
| 冷启动-自动 | torchvision | NA | python版本<3.12：0.15.0 | python版本<3.12：0.15.0  python版本==3.12：0.17.0 |
| 冷启动-自动 | setuptools | NA | python 版本 < 3.12: python 自带  python版本==3.12：80.9.0 | python 版本 < 3.12: python 自带  python版本==3.12：80.9.0 |
| 折叠机UX规则检测 | numpy | NA | NA | 1.26.4 |
| 折叠机UX规则检测 | ImageHash | NA | NA | 4.3.1 |
| 折叠机UX规则检测 | opencv-python | NA | NA | 4.10.0.84 |
| 折叠机UX规则检测 | paddlepaddle | NA | NA | python版本<3.12：2.6.2  python版本==3.12：3.0.0 |
| 折叠机UX规则检测 | paddleocr | NA | NA | 2.8.1 |
| 折叠机UX规则检测 | psutil | NA | NA | 5.9.8 |
| 折叠机UX规则检测 | Werkzeug | NA | NA | 3.1.3 |
| 折叠机UX规则检测 | scikit-learn | NA | NA | 1.5.1 |
| 折叠机UX规则检测 | supervision | NA | NA | 0.17.1 |
