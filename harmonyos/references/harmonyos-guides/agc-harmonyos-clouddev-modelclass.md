---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-modelclass
title: (可选）一键生成Model Class
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > (可选）一键生成Model Class
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:21+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:655fe55bd5a07dfd00fe3ea857c75a999f13515e46596ff84053c7e097dc5b8d
---

云数据库支持从端侧或者云侧云函数（含云对象）访问云数据库，代码涉及调用云数据库时，需引入对应云数据库对象类型的Model Class。当前支持为对象类型一键生成Server Model与Client Model，供您在端侧及云侧云函数（含云对象）开发时引用。

## 生成Server Model

1. 右击需要调用的对象类型文件（以“Post.json”为例），选择“Generate Server Model”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/2A7_xDenQYWnhxSkaeLaRQ/zh-cn_image_0000002214704509.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=B65905A0E2B021CCEAEAD737F0D2847E4E9B6E6CB7257461E65C375C69E7BD72)
2. 选择生成的Server Model文件存放的云函数（或云对象）目录，以“id-generator”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/YozW-HbdSsGULFvMxTFUaA/zh-cn_image_0000002214704513.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=18F11DC09855E5457C0DC51E3BC0A941A803F2F757D88C910D077F1E645928B3)
3. 点击“OK”。

   指定目录下生成对应对象类型的Server Model文件，后续您便可以在代码中方便地引用该Server Model 。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/DT3mSE5oRZCSBRrqGhsHDA/zh-cn_image_0000002179498268.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F0A9989BB6EEF67C964ED879B5D0C18C7AB284E5A862CEA26C99ECBBCF455B3)
4. 在云对象“id-generator”目录的package.json文件中引入@hw-agconnect/cloud-server依赖。

   ```typescript
   "dependencies": {
     "@hw-agconnect/cloud-server": "latest"
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/jDpDXiOmQAuYT8ocRk9ldQ/zh-cn_image_0000002308906729.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=70A868E62DEA14EBFC46B6C516BC41AF792E99C0FF85B0EBEC0F3DEF2DA6100D)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/juNwXmbTQAa_USLEs3de9w/zh-cn_image_0000002214858901.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=94B5F604594DDD16D94D338C9AF6A27D4B69080DC31E6EE5B42107921B9C1542)
2. 选择生成的Client Model文件存放的端侧目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/q-VcVcxoT76AvGhOweKNhQ/zh-cn_image_0000002214858897.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=970CBCEF1F05C37DF4DF64F9875C14580D5E201607003FE863F8C965273AAA15)
3. 点击“OK”。

   指定目录下生成对应对象类型的Client Model文件，后续您便可以在端侧代码中方便地引用该Client Model，具体可参考端云一体化工程初始化代码中的Client Model示例（“ets/pages/CloudDb/Post.ts”）在CloudDb.ets以及DbInset.ets中的引用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/ZthYXk2yR-WPSZjBXw1D9g/zh-cn_image_0000002179338564.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=E970EFB39922CCD2F227FE53964F74754D85B5F7CAB8B335CE096BDC8A272841)
