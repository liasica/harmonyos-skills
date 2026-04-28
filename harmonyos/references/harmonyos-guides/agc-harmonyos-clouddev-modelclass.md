---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-modelclass
title: (可选）一键生成Model Class
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > (可选）一键生成Model Class
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:06+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:74482e71d9eef64b8571531232e07661b517184c2d6658167ffea4e62dea198e
---

云数据库支持从端侧或者云侧云函数（含云对象）访问云数据库，代码涉及调用云数据库时，需引入对应云数据库对象类型的Model Class。当前支持为对象类型一键生成Server Model与Client Model，供您在端侧及云侧云函数（含云对象）开发时引用。

## 生成Server Model

1. 右击需要调用的对象类型文件（以“Post.json”为例），选择“Generate Server Model”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/DcBpdzijQnm2LyLdgKtAjQ/zh-cn_image_0000002214704509.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=A25024FFCA898960E0C04C56F801F0B601F2670E95B4ECC5974E125E18ED65E5)
2. 选择生成的Server Model文件存放的云函数（或云对象）目录，以“id-generator”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/zFMjb_wzR1OlbpNn4f-pSQ/zh-cn_image_0000002214704513.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=2BA5E39E60E4B5ADAF7CE1C6D2B468AB5B647E5AAA1FC52E6AD9CC84635EDEF5)
3. 点击“OK”。

   指定目录下生成对应对象类型的Server Model文件，后续您便可以在代码中方便地引用该Server Model 。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/8h6Zf_t8QbKY3ov7Qc-mwA/zh-cn_image_0000002179498268.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=BCEB12BA764409FA3A3A006495051788E130AE1C8FE9DC7A65572EB8BF978697)
4. 在云对象“id-generator”目录的package.json文件中引入@hw-agconnect/cloud-server依赖。

   ```
   1. "dependencies": {
   2. "@hw-agconnect/cloud-server": "latest"
   3. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/d1R4E3HPShCzDaWTpRizog/zh-cn_image_0000002308906729.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=7BF433B3EFDE61FB2830F22A9411A5F34A9F90C6709E6FB632DDD7CC30A5C7F6)
5. 在云对象文件idGenerator.ts中添加如下代码，实现云函数访问云数据库。

   ```
   1. import { cloud } from '@hw-agconnect/cloud-server';
   2. import { Post } from './Post'; // Post是Server Model

   4. // Demo是Post对象类型使用的存储区名
   5. const collection = cloud.database({ zoneName: 'Demo' }).collection(Post);

   7. // IdGenerator云对象，实现了对Post对象类型的查询和更新
   8. export class IdGenerator {
   9. query() {
   10. return collection.query().get();
   11. }

   13. upsert(posts: Post[]) {
   14. return new Promise((resolve, reject) => {
   15. collection.upsert(posts.map(post => Post.parseFrom(post)))
   16. .then(result => resolve({ result }))
   17. .catch(err => reject(err))
   18. });
   19. }
   20. }
   ```

   注意

   如果定义的云数据库表字段中包含ByteArray或Date类型的字段，在插入或者更新云数据库时需要使用Server Model的parseFrom方法将入参转化成API识别的类型，例如上述示例中的Post.parseFrom方法。

## 生成Client Model

1. 右击需要调用的对象类型文件（以“Post.json”为例），选择“Generate Client Model”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/CMPmHVTrS_mlAFyrJcC77g/zh-cn_image_0000002214858901.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=F59598D8A5A9D9F4E29782ACB9C734D296566461A01CCDEDB37D723E534F499D)
2. 选择生成的Client Model文件存放的端侧目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/vk9Spsp1QcOYxKu1J_TONA/zh-cn_image_0000002214858897.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=CA7DCBF9FE6FB87EDCC92D70E9CB9ED5169195D1C33EBEE230D7FB42AD349E26)
3. 点击“OK”。

   指定目录下生成对应对象类型的Client Model文件，后续您便可以在端侧代码中方便地引用该Client Model，具体可参考端云一体化工程初始化代码中的Client Model示例（“ets/pages/CloudDb/Post.ts”）在CloudDb.ets以及DbInset.ets中的引用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/kelFk8UEQhu5yh6pQeOcXw/zh-cn_image_0000002179338564.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=A25C0079D73148928A3B7AF4FCAC0875FB9DFF3F5121AB96BF2E973CF5C15DED)
