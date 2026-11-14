---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-modelclass
title: (可选）一键生成Model Class
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > (可选）一键生成Model Class
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:49+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:ed64b3aaa11f5eff9ce084d3b43d278b9922e7ad78e7a0a0df0abc4e31732ad2
---

云数据库支持从端侧或者云侧云函数（含云对象）访问云数据库，代码涉及调用云数据库时，需引入对应云数据库对象类型的Model Class。当前支持为对象类型一键生成Server Model与Client Model，供您在端侧及云侧云函数（含云对象）开发时引用。

## 生成Server Model

1. 右击需要调用的对象类型文件（以“Post.json”为例），选择“Generate Server Model”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/kCscwbtPQxeGWLAlviNvww/zh-cn_image_0000002214704509.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=29F8358051620A0780E8042BF16C5A30DA210DFCAF40A7D2C355C9F5546ED765)
2. 选择生成的Server Model文件存放的云函数（或云对象）目录，以“id-generator”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/HqrE9k6eT-ap21Mlwz8waQ/zh-cn_image_0000002214704513.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0448DEBEA8F54DBC91CEC60108036D14057BB1AAB2C10678097E913A3F2D9FA)
3. 点击“OK”。

   指定目录下生成对应对象类型的Server Model文件，后续您便可以在代码中方便地引用该Server Model 。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/jRGTYfCtTImQu9SR_wPZVQ/zh-cn_image_0000002179498268.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=5803E61CD63B8524558CB6BDE68E7B929585BB17969F1BEEE18895CE6B7334C0)
4. 在云对象“id-generator”目录的package.json文件中引入@hw-agconnect/cloud-server依赖。

   ```typescript
   "dependencies": {
     "@hw-agconnect/cloud-server": "latest"
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/lSznhjDISRW5A9248VfsjQ/zh-cn_image_0000002308906729.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C7D12BEC18E1C3AF2FA4D3FAF692D47E6CEBE4943413611A63D3E458B14AF8F)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/W0HWl8xaSsyn7fYV0s_wxQ/zh-cn_image_0000002214858901.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=F511D205834D018D02C5439B1B38B957C261E66EEE8FAAF31793051943ADBA40)
2. 选择生成的Client Model文件存放的端侧目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/g51UGdWIR9ODanq9DAIguw/zh-cn_image_0000002214858897.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=A851B00FF75C18419154701EEC77411EE37E66BE84D1C61C11C213D9A927E4A9)
3. 点击“OK”。

   指定目录下生成对应对象类型的Client Model文件，后续您便可以在端侧代码中方便地引用该Client Model，具体可参考端云一体化工程初始化代码中的Client Model示例（“ets/pages/CloudDb/Post.ts”）在CloudDb.ets以及DbInset.ets中的引用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Y4MGog7WT9exvxtMi3541w/zh-cn_image_0000002179338564.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B245080AE3FA87CECBA79292776427D001A6E01BF54E137680B2FE5FB99DFE4)
