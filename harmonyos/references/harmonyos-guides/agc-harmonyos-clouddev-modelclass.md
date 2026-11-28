---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-modelclass
title: (可选）一键生成Model Class
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > (可选）一键生成Model Class
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:29+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:db65e0e00aa7e3f22888b84e52bd8f01ee3df29ac70bd0c216787a6a0fcb6a98
---

云数据库支持从端侧或者云侧云函数（含云对象）访问云数据库，代码涉及调用云数据库时，需引入对应云数据库对象类型的Model Class。当前支持为对象类型一键生成Server Model与Client Model，供您在端侧及云侧云函数（含云对象）开发时引用。

## 生成Server Model

1. 右击需要调用的对象类型文件（以“Post.json”为例），选择“Generate Server Model”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/0Q6hTLakStqLiW3fj92g6Q/zh-cn_image_0000002214704509.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=C679ECF35A7CE2D871B41ADD0E7BE1C365AB9F37FA92928E547FD2E5BA673EA6)
2. 选择生成的Server Model文件存放的云函数（或云对象）目录，以“id-generator”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/EOTTAfrIQRuRvOi4DChYGA/zh-cn_image_0000002214704513.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=04775C3E5DED7A98242C5B472645C3CCE53B067BBCBE6BA012EE16483C9C4002)
3. 点击“OK”。

   指定目录下生成对应对象类型的Server Model文件，后续您便可以在代码中方便地引用该Server Model 。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/kcJ16N1zQnipqroLA-vDlQ/zh-cn_image_0000002179498268.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF6EE699D644CB035B4C1960D2B4B4BE3C7B64DDB34BA5350E50ECE15BDE348D)
4. 在云对象“id-generator”目录的package.json文件中引入@hw-agconnect/cloud-server依赖。

   ```typescript
   "dependencies": {
     "@hw-agconnect/cloud-server": "latest"
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/tGDj5jP2Qfi45NYew9YKqw/zh-cn_image_0000002308906729.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=354E62445DE8BC3B39CB65D57D0C928C10FB4F7C8BC5E16E140749DB6C2A7BA8)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/v7yUMvwVTv6ko4Wguv9zMw/zh-cn_image_0000002214858901.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E1BDFE3DCF05F257FDEED2EB3711E2BDC77602628F0C8F20EBEE421988CB074)
2. 选择生成的Client Model文件存放的端侧目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/GYq1-W6OSxifCRnr5HGZdw/zh-cn_image_0000002214858897.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=681978DB37B9F514060D4558D86B0E0FBAAECBE60163809F9A32C7899053FC3E)
3. 点击“OK”。

   指定目录下生成对应对象类型的Client Model文件，后续您便可以在端侧代码中方便地引用该Client Model，具体可参考端云一体化工程初始化代码中的Client Model示例（“ets/pages/CloudDb/Post.ts”）在CloudDb.ets以及DbInset.ets中的引用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/GBzMytTMSO2blLiKnqreoQ/zh-cn_image_0000002179338564.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=263A9CEB0464DCAB315AD4355CDA5E149540A06370E064B7E635C139251A13D7)
