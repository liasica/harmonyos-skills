---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/build-with-ndk-cmake
title: 使用命令行CMake构建NDK工程
breadcrumb: 指南 > NDK开发 > 构建NDK工程 > 使用命令行CMake构建NDK工程
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:61e5b43c62b3d2d0475bec65df215da85b1a27a2387bf02eb7c9b6e4fad2fe60
---

在很多复杂应用工程中，C++代码工程是通过CMake等构建系统以命令行方式来编译构建的，接下来介绍如何把已有的CMake工程切换到HarmonyOS工具链中，从而使用命令行CMake构建该工程。

## 获取NDK开发包

1. 通过下载command line tools获取NDK开发包。

   先下载command line tools并解压完成，NDK开发相关工具位于$command line tools解压目录/sdk/default/openharmony/native路径下。
2. 通过安装DevEco Studio获取NDK开发包。

   先下载并安装完成DevEco Studio，NDK开发相关工具位于$DevEco Studio安装目录/sdk/default/openharmony/native路径下。

### 配置环境变量

如果只是在DevEco Studio中使用，跳过以下步骤：

1. 将NDK自带的CMake编译工具添加到环境变量中。

   * 配置 linux 系统下环境变量

     ```
     1. # 打开.bashrc文件
     2. vim ~/.bashrc
     3. # 在文件最后添加cmake路径，该路径是自己的放置文件的路径，之后保存退出
     4. export PATH=${实际SDK路径}/native/build-tools/cmake/bin:$PATH
     5. # 在命令行执行source ~/.bashrc使环境变量生效
     6. source ~/.bashrc
     ```
   * 配置 mac 系统下环境变量

     ```
     1. #在当前用户目录下，打开 .bash_profile 文件，文件如果不存在，创建即可
     2. vim ~/.bash_profile
     3. #在文件最后添加 cmake 路径，该路径是自己的放置文件的路径，之后保存退出
     4. export PATH=${实际SDK路径}/native/build-tools/cmake/bin:$PATH
     5. #在命令行执行 source ~/.bash_profile 使环境变量生效
     6. source ~/.bash_profile
     ```
   * 配置 windows 下的环境变量

     右键点击我的电脑，在下拉框中选择【属性】，然后点击【高级系统设置】，进入【环境变量】，找到【Path】并点击【编辑】，接着点击【新建】添加路径，保存后退出。最后打开cmd（若下一步不能够实现，请重启电脑尝试）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/vAQSuSt5TMOhs5BA46Yr6A/zh-cn_image_0000002558765858.png?HW-CC-KV=V1&HW-CC-Date=20260429T054353Z&HW-CC-Expire=86400&HW-CC-Sign=A42C7ED76DEF24B32BC28ACD4A907FE9D0C995DE2DB519374D83A2EFDE130676)

     打开命令框，输入cmake.exe -version，命令行正确回显cmake的版本号，说明环境变量配置完成。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/y2x0yX2hSr-05KspNUhq6w/zh-cn_image_0000002558606202.png?HW-CC-KV=V1&HW-CC-Date=20260429T054353Z&HW-CC-Expire=86400&HW-CC-Sign=2F6287E428843720A62CB4B3CFBF2E0E89639BDDD27C0E8FBF4530FAF7A28798)
2. 查看CMake默认路径。

   * linux 和 mac 系统环境下

     ```
     1. #在命令行输入which命令查询当前CMake所在路径
     2. which cmake
     3. #结果路径与.bashrc中设置一致
     4. ~/ohos-sdk/ohos-sdk/linux/native/build-tools/cmake/bin/cmake
     ```
   * windows 系统环境下，cmake 安装路径为自己所配置的环境变量路径

     通过 我的电脑->高级系统设置->环境变量->在 Path 对象中查看

## 使用NDK开发包编译Native程序

应用开发者可以通过NDK开发包快速开发出Native动态库、静态库与可执行文件。NDK开发包提供CMake编译构建工具脚本，下面通过编写一个C/C++ demo工程来演示适配过程。

### demo工程内容

下面是一个CMake的demo工程内容，此工程包含两个目录，include目录包含此库的头文件，src目录包含全部源码；src目录包含两个文件，sum.cpp的算法文件，以及hello.cpp的调用算法的主入口文件，目标是编译成一个可执行程序，以及一个算法动态库。

**demo目录图**

```
1. demo
2. ├── CMakeLists.txt
3. ├── include
4. └── sum.h
5. └── src
6. ├── CMakeLists.txt
7. ├── sum.cpp
8. └── hello.cpp
```

**根目录CMakeLists.txt内容**

```
1. # 指定CMake的最小版本
2. CMAKE_MINIMUM_REQUIRED(VERSION 3.16)

4. # 工程名称，这里我们就叫HELLO
5. PROJECT(HELLO)

7. #添加一个子目录并构建该子目录。
8. ADD_SUBDIRECTORY(src)
```

**内部CMakeLists.txt内容**

```
1. SET(LIBHELLO_SRC hello.cpp)

3. # 设置编译参数
4. SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0")

6. # 设置链接参数，具体参数可以忽略，纯粹为了举例
7. SET(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,--emit-relocs --verbose")

9. # 添加一个libsum动态库目标，编译成功会生成一个libsum.so
10. ADD_LIBRARY(sum SHARED sum.cpp)

12. # 生成可执行程序，添加一个Hello的可执行程序目标，编译成功会生成一个Hello可执行程序
13. ADD_EXECUTABLE(Hello ${LIBHELLO_SRC})

15. # 指定Hello目标include目录路径
16. TARGET_INCLUDE_DIRECTORIES(Hello PUBLIC ../include)

18. # 指定Hello目标需要链接的库名字
19. TARGET_LINK_LIBRARIES(Hello PUBLIC sum)
```

**源码内容**

hello.cpp源码

```
1. #include <iostream>
2. #include "sum.h"

4. int main(int argc,const char **argv)
5. {
6. std::cout<< "hello world!" <<std::endl;
7. int total = sum(1, 100);
8. std::cout<< "Sum 1 + 100=" << total << std::endl;
9. return 0;
10. }
```

sum.h源码

```
1. int sum(int a, int b);
```

sum.cpp源码

```
1. #include <iostream>

3. int sum(int a, int b)
4. {
5. return a + b;
6. }
```

### 编译构建demo工程

**linux 和 mac 系统环境下**

在工程目录的模块目录下，创建build目录，用来放置CMake构建时产生的中间文件。注意: ohos-sdk是下载下来的SDK的根目录，开发者需要自行替换成实际的下载目录。

1. 采用OHOS\_STL=c++\_shared动态链接c++库方式构建工程，如不指定，默认采用c++\_shared；OHOS\_ARCH参数可根据系统架构来决定具体值，例如当OHOS\_ARCH=armeabi-v7a会编译32位动态库，而当OHOS\_ARCH=arm64-v8a会编译64位动态库。

   ```
   1. >mkdir build && cd build
   2. >cmake -D OHOS_STL=c++_shared -D OHOS_ARCH=arm64-v8a -D OHOS_PLATFORM=OHOS -D CMAKE_TOOLCHAIN_FILE={ohos-sdk}/linux/native/build/cmake/ohos.toolchain.cmake ..
   3. >cmake --build .
   ```
2. 采用OHOS\_STL=c++\_static静态链接c++库方式构建工程，当OHOS\_ARCH=armeabi-v7a会编译32位静态库，而当OHOS\_ARCH=arm64-v8a会编译64位静态库。

   ```
   1. >mkdir build && cd build
   2. >cmake -D OHOS_STL=c++_static -D OHOS_ARCH=arm64-v8a -D OHOS_PLATFORM=OHOS -D CMAKE_TOOLCHAIN_FILE={ohos-sdk}/linux/native/build/cmake/ohos.toolchain.cmake ..
   3. >cmake --build .
   ```

   命令中，OHOS\_ARCH与OHOS\_PLATFORM两个变量最终会生成clang++的--target命令参数，在此例子中就是--target=arm-linux-ohos和--march=armv7a两个参数。

   CMAKE\_TOOLCHAIN\_FILE指定了toolchain文件，在此文件中默认给clang++设置了--sysroot={ndk\_sysroot目录}，告诉编译器查找系统头文件的根目录。

注意

动态链接在运行时加载库文件，能有效节省磁盘空间和内存，但也增加运行时加载开销，略微影响启动性能。静态链接则将库代码直接嵌入可执行文件，启动快，但生成的文件体积更大，适合对启动性能敏感或运行环境受限的场景，不适用于对磁盘空间敏感的应用或设备。

**windows系统环境下**

在windows下使用cmake进行编译，与linux下不同的是，使用cmake要加入参数 -G 选择使用的生成器，直接回车会列出下面的生成器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/jWG4P1A_TLW4kqMiLcfORg/zh-cn_image_0000002589325729.png?HW-CC-KV=V1&HW-CC-Date=20260429T054353Z&HW-CC-Expire=86400&HW-CC-Sign=1BF91E17802F2E0D58D372401C43D3D298191749B568D726E69927DA34E5DCE8)

这里使用的是cmake .. -G "Ninja" 引号里面跟的参数就是上图查看的环境所支持的生成器，这里ndk中自带的生成器是Ninja。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/hfiWZp8fSUWJDX_vOU_bXQ/zh-cn_image_0000002589245669.png?HW-CC-KV=V1&HW-CC-Date=20260429T054353Z&HW-CC-Expire=86400&HW-CC-Sign=7BCD3A8DE1C9CEE35F777B69A3FADF32DA2978E0E90251F26FD363DDF75E8D42)

Step 1. 同样在工程目录的模块目录下创建 build 文件夹，进入build目录并执行以下指令：

```
1. F:\windows\native\build-tools\cmake\bin\cmake.exe -G "Ninja" -D OHOS_STL=c++_shared -D OHOS_ARCH=arm64-v8a -D OHOS_PLATFORM=OHOS -D CMAKE_TOOLCHAIN_FILE=F:\windows\native\build\cmake\ohos.toolchain.cmake ..
```

注意

如需debug调试，增加参数 -D CMAKE\_BUILD\_TYPE=Debug；cmake路径和编译工具链ohos.toolchain.cmake路径都是下载好的ndk路径。

执行结果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/p53GIBkbTASqyVNx18sPfg/zh-cn_image_0000002558765860.png?HW-CC-KV=V1&HW-CC-Date=20260429T054353Z&HW-CC-Expire=86400&HW-CC-Sign=39ECF161F4A620F2A4D0F96706EDADDF89EC7559AA6E131479ED32E59D30924E)

这里生成的build.ninja文件就是我们需要的 。

Step 2. 让我们用ninja指令来编译生成目标文件，其位置如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/6HWWG8jSRBaUWueFa-6viw/zh-cn_image_0000002558606204.png?HW-CC-KV=V1&HW-CC-Date=20260429T054353Z&HW-CC-Expire=86400&HW-CC-Sign=C3736923F00E5F405706C2A624B4386F8A5673AFC75CCBD4036EA7EC2DB24FBE)

ninja -f build.ninja 或者用 cmake --build . 执行结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/UJo1Tir2R6eUzbgcOIFjaQ/zh-cn_image_0000002589325731.png?HW-CC-KV=V1&HW-CC-Date=20260429T054353Z&HW-CC-Expire=86400&HW-CC-Sign=0FD83939673DA131A9552A19D88B849CF9D020AC453B2C85BD6DD79E01B8B9FC)

编译生成的可执行文件位于创建的build目录下的src目录中。
