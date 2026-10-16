---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-modelclass
title: (可选）一键生成Model Class
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > (可选）一键生成Model Class
category: harmonyos-guides
scraped_at: 2026-10-17T06:43:18+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:7c68c378a6f965a77020aaa0da81e1165dbd2a2c86891772d0b4d94ff1ee0b07
---

云数据库支持从端侧或者云侧云函数（含云对象）访问云数据库，代码涉及调用云数据库时，需引入对应云数据库对象类型的Model Class。当前支持为对象类型一键生成Server Model与Client Model，供您在端侧及云侧云函数（含云对象）开发时引用。

## 生成Server Model

1. 右击需要调用的对象类型文件（以“Post.json”为例），选择“Generate Server Model”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/1_k3xgEFTOqCHjuUW7sTnA/zh-cn_image_0000002214704509.png)
2. 选择生成的Server Model文件存放的云函数（或云对象）目录，以“id-generator”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/kYe6rw7xT0-RNyHFhmmzBg/zh-cn_image_0000002214704513.png)
3. 点击“OK”。

   指定目录下生成对应对象类型的Server Model文件，后续您便可以在代码中方便地引用该Server Model 。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/XFh6AEOzT6-xJNPXTveh9Q/zh-cn_image_0000002179498268.png)
4. 在云对象“id-generator”目录的package.json文件中引入@hw-agconnect/cloud-server依赖。

   ```typescript
   "dependencies": {
     "@hw-agconnect/cloud-server": "latest"
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/Uh6l4l0zTiGNHGFHwDaPXA/zh-cn_image_0000002308906729.png)
5. 在云对象文件idGenerator.ts中添加如下代码，实现云函数访问云数据库。

   ```screen
   import { cloud } from '@hw-agconnect/cloud-server'; 
   import { Post } from './Post'; // Post是Server Model 

   // Demo是Post对象类型使用的存储区名
   const collection = cloud.database({ zoneName: 'Demo' }).collection(Post);

   // IdGenerator云对象，实现了对Post对象类型的查询和更新
   export class IdGenerator {
     query() {
       return collection.query().get();
     }

     upsert(posts: Post[]) {
       return new Promise((resolve, reject) => {
         collection.upsert(posts.map(post => Post.parseFrom(post)))
           .then(result => resolve({ result }))
           .catch(err => reject(err))
       });
     }
   }
   ```

   **注意** 

   如果定义的云数据库表字段中包含ByteArray或Date类型的字段，在插入或者更新云数据库时需要使用Server Model的parseFrom方法将入参转化成API识别的类型，例如上述示例中的Post.parseFrom方法。

## 生成Client Model

1. 右击需要调用的对象类型文件（以“Post.json”为例），选择“Generate Client Model”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/URAV1oYmSj-kkQ5NRKXXRQ/zh-cn_image_0000002214858901.png)
2. 选择生成的Client Model文件存放的端侧目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/F6F4XFE_SK6jboWN1d2Wig/zh-cn_image_0000002214858897.png)
3. 点击“OK”。

   指定目录下生成对应对象类型的Client Model文件，后续您便可以在端侧代码中方便地引用该Client Model，具体可参考端云一体化工程初始化代码中的Client Model示例（“ets/pages/CloudDb/Post.ts”）在CloudDb.ets以及DbInset.ets中的引用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/a1dBsjokQvW2Hox1FdDMHA/zh-cn_image_0000002179338564.png)
