---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-modelclass
title: (可选）一键生成Model Class
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > (可选）一键生成Model Class
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:03+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4fcc86d07c0f3b52376a22712dc634b5b8b2528e2daefdf18f5d3528f56b3b96
---

云数据库支持从端侧或者云侧云函数（含云对象）访问云数据库，代码涉及调用云数据库时，需引入对应云数据库对象类型的Model Class。当前支持为对象类型一键生成Server Model与Client Model，供您在端侧及云侧云函数（含云对象）开发时引用。

## 生成Server Model

1. 右击需要调用的对象类型文件（以“Post.json”为例），选择“Generate Server Model”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/4WLCFCruRyebqD6j6nX4Og/zh-cn_image_0000002214704509.png)
2. 选择生成的Server Model文件存放的云函数（或云对象）目录，以“id-generator”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/JBKnpVjbRyqKNHxZfa2W1g/zh-cn_image_0000002214704513.png)
3. 点击“OK”。

   指定目录下生成对应对象类型的Server Model文件，后续您便可以在代码中方便地引用该Server Model 。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/Luscw89nTo2buhuAX9MTog/zh-cn_image_0000002179498268.png)
4. 在云对象“id-generator”目录的package.json文件中引入@hw-agconnect/cloud-server依赖。

   ```
   1. "dependencies": {
   2. "@hw-agconnect/cloud-server": "latest"
   3. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/oFn8VeouTuGU6PjVznNERg/zh-cn_image_0000002308906729.png)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/M0Z03k6YTnSOUQftva6ezw/zh-cn_image_0000002214858901.png)
2. 选择生成的Client Model文件存放的端侧目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/ix6OlTlbTWG3NSpFJXcaCg/zh-cn_image_0000002214858897.png)
3. 点击“OK”。

   指定目录下生成对应对象类型的Client Model文件，后续您便可以在端侧代码中方便地引用该Client Model，具体可参考端云一体化工程初始化代码中的Client Model示例（“ets/pages/CloudDb/Post.ts”）在CloudDb.ets以及DbInset.ets中的引用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/oVkxSBazTX20p9sp_RvvtA/zh-cn_image_0000002179338564.png)
