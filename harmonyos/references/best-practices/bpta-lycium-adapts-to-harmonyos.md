---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-lycium-adapts-to-harmonyos
title: 使用lycium工具快速编译三方库
breadcrumb: 最佳实践 > 编译构建 > 使用lycium工具快速编译三方库
category: best-practices
scraped_at: 2026-04-29T14:14:22+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:d6ee60a4040239775b18dc889edb49435d7d551f7387e267fc627f6646c6dffa
---

## 概述

随着技术的不断发展，移动应用开发需求也越来越大，在传统移动应用开发过程中，开发者需要面对较为繁琐的配置和环境搭建，这使开发成本变得更高。为解决这类问题，通过使用[lycium](https://gitcode.com/openharmony-sig/tpc_c_cplusplus/tree/master/lycium)工具，可以帮助开发者实现快速开发，简化开发流程，减少开发耗时。

lycium是一款协助开发者通过shell语言实现C/C++三方库快速交叉编译，并在HarmonyOS上快速验证的编译框架工具。

开发者只需要设置对应C/C++三方库的编译方式以及编译参数，通过lycium就能快速的构建出能在HarmonyOS上运行的二进制文件。

本文将以openssl为例，介绍如何通过lycium工具快速编译三方库。

## 通过lycium工具快速编译三方库

本小节介绍如何在Linux环境下，使用lycium工具通过ohos sdk快速编译openssl三方库源码。

## 编译环境准备

1. Linux编译环境搭建及HarmonyOS SDK下载，请参考：[环境准备](bpta-cmake-adapts-to-harmonyos.md#section197241001402)。
2. 下载完SDK后，将SDK工具链配置到环境变量中。
   1. lycium支持的是C/C++三方库的交叉编译，SDK工具链只涉及到native目录下的工具，故OHOS\_SDK的路径需配置成native工具的父目录，Linux环境中配置SDK环境变量方法如下：

      ```
      1. owner@ubuntu:/mnt/e$ export OHOS_SDK=/xxx/ohos-sdk/linux # 此处SDK的路径需要开发者配置成自己的sdk解压目录
      ```
   2. 拷贝编译工具。

      为简化开发中命令的配置，针对arm架构以及aarch64架构集成了几个编译命令，存放在lycium/Buildtools目录下。在使用lycium工具前，需要将这些编译命令拷贝到SDK对应的目录下，具体操作如下：

      ```
      1. owner@ubuntu:/mnt/e/tpc_c_cplusplus-master$ cd lycium/Buildtools # 进入到工具包目录
      2. owner@ubuntu:/mnt/e/tpc_c_cplusplus-master/lycium/Buildtools$ sha512sum -c SHA512SUM # 可校验工具包是否正常, 若输出"toolchain.tar.gz: OK"则说明工具包正常，否则说明工具包异常，需重新下载
      3. owner@ubuntu:/mnt/e/tpc_c_cplusplus-master/lycium/Buildtools$ tar -zxvf toolchain.tar.gz # 解压拷贝编译工具
      4. owner@ubuntu:/mnt/e/tpc_c_cplusplus-master/lycium/Buildtools$ cp toolchain/* ${OHOS_SDK}/native/llvm/bin # 将命令拷贝到工具链的native/llvm/bin目录下
      ```
   3. 若SDK中cmake版本较低（cmake推荐使用3.26及以上版本），升级SDK即可。

## 编译三方库

1. 修改三方库的编译方式以及编译参数。

   lycium框架提供了HPKBUILD文件供开发者对相应的C/C++三方库的编译配置。

   1. 在thirdparty目录下新建文件夹，用于存放三方库文件和HPKBUILD文件。

      ```
      1. owner@ubuntu:/mnt/e/tpc_c_cplusplus-master/thirdparty$ mkdir openssl
      ```
   2. 将HPKBUILD模板文件拷贝到新建三方库目录下。

      ```
      1. owner@ubuntu:/mnt/e/tpc_c_cplusplus-master/thirdparty$ cp /xxx/tpc_c_cplusplus-master/lycium/template/HPKBUILD openssl
      ```
   3. 根据三方库实际情况修改HPKBUILD文件配置项。

      ```
      1. pkgname=NAME # 库名(必填)
      2. pkgver=VERSION # 库版本(必填)
      3. source="https://downloads.sourceforge.net/$pkgname/$pkgname-$pkgver.tar.gz" # 库源码下载链接(必填)
      4. buildtools= # 编译方法, 暂时支持cmake, configure, make等, 根据三方库的编译构建方式填写.(必填)
      5. builddir= # 源码压缩包解压后目录名(必填)
      6. # 省略部分配置项
      7. # 编译前准备工作，如设置环境变量，创建编译目录等
      8. prepare() {
      9. }

      11. # 执行编译构建的命令
      12. build() {
      13. }

      15. # 安装打包
      16. package() {
      17. }

      19. # 测试
      20. check() {
      21. }

      23. # 清理环境
      24. cleanbuild() {
      25. }
      ```

      每个编译脚本都需要按照该规则定义相应的变量以及对应的5个函数，其中变量标明必填的，需要根据库信息正确填写，否则会导致编译失败。

      填写示例参考如下：

      openssl的编译构建方式是configure编译构建，configure交叉编译是需要配置host类型，且需要配置对应的环境变量，框架中集成了环境变量设置的接口，封装在envset.sh中，因此除了基本信息外，还需要定义一个host变量以及导入envset.sh文件，基本变量配置参考如下：

      ```
      1. pkgname=openssl # 库名
      2. pkgver=OpenSSL_1_1_1u # 库的版本号
      3. source="https://github.com/openssl/$pkgname/archive/refs/tags/$pkgver.zip" # 库的源码包路径
      4. archs=("armeabi-v7a" "arm64-v8a") # 架构信息
      5. buildtools="configure" # 编译方式为configure
      6. builddir=$pkgname-${pkgver} # openssl 源码包解压后的文件夹名
      7. packagename=$builddir.zip # 包名
      8. source envset.sh # 导入envset.sh，envset.sh为环境设置脚本文件，通常包含构建所需的变量和函数，存放于tpc_c_cplusplus/lycium/script目录下
      9. host= # 定义host变量
      ```

      在prepare()函数中创建编译目录，配置对应架构的环境变量：

      ```
      1. prepare() {
      2. mkdir -p $builddir/$ARCH-build
      3. if [ $ARCH == ${archs[0]} ] # $ARCH：环境变量，表示目标架构，用于区分不同的CPU架构
      4. then
      5. setarm32ENV
      6. host=linux-generic32
      7. elif [ $ARCH == ${archs[1]} ]
      8. then
      9. setarm64ENV
      10. host=linux-aarch64
      11. else
      12. echo "${ARCH} not support"
      13. return -1
      14. fi
      15. }
      ```

      build()函数使用configure命令生成Makefile并执行make指令：

      ```
      1. build() {
      2. cd $builddir/$ARCH-build
      3. ../Configure $* $host > `pwd`/build.log 2>&1
      4. make -j4 >> `pwd`/build.log 2>&1
      5. ret=$?
      6. cd $OLDPWD
      7. return $ret
      8. }
      ```

      openssl测试时需要单独通过编译目标depend生成测试用例，因此需要修改对应的check()函数。在check函数中执行make depend，并在执行完后清理对应的环境变量，以及在该函数后面通过注释说明该库在设备上的测试方法。

      ```
      1. check() {
      2. cd $builddir/$ARCH-build
      3. make depend >> `pwd`/build.log 2>&1
      4. cd $OLDPWD
      5. if [ $ARCH == ${archs[0]} ]
      6. then
      7. unsetarm32ENV
      8. fi
      9. if [ $ARCH == ${archs[1]} ]
      10. then
      11. unsetarm64ENV
      12. fi
      13. unset host
      14. echo "Test must be on HarmonyOS device!"
      15. # real test CMD
      16. # 将编译目录加到 LD_LIBRARY_PATH 环境变量
      17. # make test
      18. }
      ```

      package()和cleanbuild()函数，使用模板默认的即可。
2. 快速编译三方库。

   配置完三方库的编译方式参数后，在lycium目录执行./build.sh openssl（openssl即为创建的目录名称），进行自动编译三方库，并打包安装到当前目录的usr/pkgname/ARCH目录（pkgname为三方库名称，ARCH为架构名称）。

   ```
   1. owner@ubuntu:/mnt/e/tpc_c_cplusplus-master/lycium$ ./build.sh openssl # 默认编译thirdparty目录下的库
   2. Build OS linux
   3. OHOS_SDK=/mnt/e/ohos-sdk/linux
   4. CLANG_VERSION=15.0.4
   5. Build openssl OpenSSL_1_1_1u start!
   6. % Total % Received % Xferd Average Speed     Time    Time     Time Current
   7. Dload  Upload    Total    Spent     Left Speed
   8. 100   222 0      222 0     0   457       0 --:--:-- --:--:-- --:--:--   456
   9. 100 11.3M 0    11.3M 0     0  958k       0 --:--:-- 0:00:12  --:--:-- 1802k
   10. Compile HarmonyOS armeabi-v7a openssl OpenSSL_1_1_1u libs...
   11. # 省略部分编译信息
   12. ALL JOBS DONE!!!
   ```

   当未报错且日志打印ALL JOBS DONE!!!时，表示三方库编译成功。
3. 查看编译后的三方库文件。

   编译成功后进入lycium/usr目录下，可查看编译生成的文件。

## 应用中集成使用三方库

1. 将三方库生成的二进制文件拷贝到应用工程目录。

   为更好管理应用集成的三方库，需要在应用工程的cpp目录新建一个thirdparty目录，将生成的二进制文件以及头文件拷贝到该目录下。

   如下图所示，xxx代表三方库名称，xxx文件夹下包含了aarch64架构以及arm架构两种方式生成的二进制文件，每种架构目录下包含了该库的头文件目录include以及二进制文件目录lib。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/INcDsvqzTEG7oQJFfIPXxA/zh-cn_image_0000002194011484.png?HW-CC-KV=V1&HW-CC-Date=20260429T061420Z&HW-CC-Expire=86400&HW-CC-Sign=52398EEF54E0A150E3537C941C904C78BB3C714534FB3A3D8037B36D0C197114)

   如果三方库二进制文件为so文件，还需要将so文件拷贝到工程目录的entry/libs/${OHOS\_ARCH}/目录下，如下图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/5a62Ot3RTwm2kX7GuZNkeA/zh-cn_image_0000002193851900.png?HW-CC-KV=V1&HW-CC-Date=20260429T061420Z&HW-CC-Expire=86400&HW-CC-Sign=B994E96E110A5ECC644F22C561EE3F1153C8BFE825598E4899333A9AA3C5E90E)

   动态库引用注意事项：

   1. 应用在引用动态库的时候是通过soname来查找的，所以开发者需要将名字为soname的库文件拷贝到entry/libs/${OHOS\_ARCH}/目录下（soname查看方法：${OHOS\_SDK}/native/llvm/bin/llvm-readelf -d libxxx.so）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/m8s4SpB8Rvi1l_N08OK5Iw/zh-cn_image_0000002193851892.png?HW-CC-KV=V1&HW-CC-Date=20260429T061420Z&HW-CC-Expire=86400&HW-CC-Sign=95905F807E12A039F3AB0076101CCE0100F43FF675D6E8EF22A246C061E46405 "点击放大")
   2. 正确拷贝so文件。

      拷贝方法：不通过压缩直接将so文件拷贝到windows，或将so文件压缩成.zip格式拷贝到windows，正确拷贝so文件后，so文件大小应该与原库实体文件大小一致。

      说明

      如果将so文件以tar、gz、7z、bzip2等压缩方式拷贝到windows后在解压，其文件是实体库的软连接，大小和实体库大小不一致，文件也不能正常使用。
2. 配置对应链接。

   配置链接只需要在cpp目录的CMakeLists.txt文件中添加对应target\_link\_libraries即可（动态库链接和静态库链接，只需填写一个）。

   * 配置静态库链接。

     ```
     1. target_link_libraries(entry PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/xxx/${OHOS_ARCH}/lib/libxxx.a)
     ```
   * 配置动态库链接。

     ```
     1. target_link_libraries(entry PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/xxx/${OHOS_ARCH}/lib/libxxx.so)
     ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/tJn1YqaQQIWfvU69PHBdvg/zh-cn_image_0000002229337281.png?HW-CC-KV=V1&HW-CC-Date=20260429T061420Z&HW-CC-Expire=86400&HW-CC-Sign=AD37D5E803BED8C686F44339719499F49DECFA82CCF841AC355D134E8638285F "点击放大")
3. 配置头文件路径。

   在cpp目录的CMakeLists.txt文件中添加对应target\_include\_directories即可：

   ```
   1. target_include_directories(entry PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/xxx/${OHOS_ARCH}/include)
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/LZoLwhxHSLe-56eam9SyOw/zh-cn_image_0000002194011488.png?HW-CC-KV=V1&HW-CC-Date=20260429T061420Z&HW-CC-Expire=86400&HW-CC-Sign=55EA206337824619AF2FBD20E725702DF1AC2B48DD55FACDCDF4680508147F28 "点击放大")
4. 配置完三方库的链接和头文件路径后，开发者即可根据自身业务逻辑，在应用中调用三方库接口，详细请参考：[三方动态链接库（.so）集成开发实践](bpta-dynamic-link-library.md)。
