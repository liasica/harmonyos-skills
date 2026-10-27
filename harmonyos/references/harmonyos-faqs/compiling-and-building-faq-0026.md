---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0026
title: 编译构建CPU与内存占用过高问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > 编译构建CPU与内存占用过高问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:51+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:33533323906d5d38787e82cbe85a2b65f536fed8e2740bb858c0bec04491cb88
---

**Q：在编译大型C++工程时，由于CPU占用率较高，可能会导致电脑卡顿和反应迟缓，应该如何处理？**

**A**：如果遇到类似问题，建议尝试以下方法进行解决：

打开模块下的build-profile.json5文件，在**arguments**参数中添加如下配置。并根据电脑CPU配置，修改compile和link的值。建议compile和link的值之和设置为CPU核数的一半，例如，如果CPU为8核，则将compile和link分别设置为2。

```json
"arguments": "-DCMAKE_JOB_POOL_COMPILE:STRING=compile -DCMAKE_JOB_POOL_LINK:STRING=link -DCMAKE_JOB_POOLS:STRING=compile=2;link=2",
```

修改了compile和link的值后，编译时间可能会延长。

**Q：编译构建时，内存或CPU占用过高，导致DevEco Studio运行卡顿和延迟。**

**A**：解决措施如下：

* 在执行hvigor构建的过程中，通过减少内存中的缓存数据、减少线程数量，可以减少编译过程中的内存占用。可以在hvigor-config.json5中添加配置。

  ```json
      {
        "modelVersion": "0.0.1",
        "dependencies": {},
        "properties": {
          // Set to 0, indicating that the memory cache configuration is not enabled. The default value is 4, and the lower the value, the less cached data in memory
          "hvigor.pool.cache.capacity": 0,
          // The default configuration is -1 CPU cores, including ohos.arkCompile.maxSize4. The smaller the value, the less memory it occupies
          "hvigor.pool.maxSize" : 5,
          // The default configuration value is 5, and the smaller the value, the less memory it occupies
          "ohos.arkCompile.maxSize": 3,
          // The default configuration value is true, indicating that the memory cache is turned on and occupies more memory. The configuration is false, and the memory cache is turned off and occupies less memory
          "hvigor.enableMemoryCache": false
        }
      }
  ```

  **说明** 

  当配置项"hvigor.pool.maxSize"和"ohos.arkCompile.maxSize"的值改小，"hvigor.enableMemoryCache"改为false后，可能会导致编译时长增加，请耐心等待。
* 如果上述修改未能达到预期效果，可以尝试使用非并行模式执行编译。
  + 在菜单栏中依次点击“File > Settings > Build, Execution, Deployment > Build Tools > Hvigor”，取消勾选“Execute tasks in parallel mode”。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/sm-QVeTZQ8uMYwaeoJhFSw/zh-cn_image_0000002772910486.png "点击放大")
  + 在命令行最后添加--no-parallel，示例：

    ```shell
            hvigorw assembleHap --no-parallel
    ```

    **说明** 

    使用非并行模式编译，内存占用将减少，但编译时间会延长，请耐心等待。
