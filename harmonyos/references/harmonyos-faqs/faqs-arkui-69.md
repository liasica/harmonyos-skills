---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-69
title: 父组件如何与孙子组件进行状态同步
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 父组件如何与孙子组件进行状态同步
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:c4bea3a9eae70a680f3eda979a656c978b31d8e6d6509d10bfb75794dad91bcf
---

* 方式一（推荐）：使用@Provider和@Consumer装饰器。在父组件中使用@Provider，在孙子组件中使用@Consumer，实现双向数据绑定。

1. 在父组件中使用子组件，并通过@Provider提供reviewVote参数，实现跨级传递到孙子组件。

   ```typescript
   @Entry
   @ComponentV2
   struct Father{
     @Provider("reviewVote") reviewVotes: number = 0;

     build() {
       Column() {
         Son()
         Button(`Father: ${this.reviewVotes}`)
       }
     }
   }
   ```
2. 在子组件中使用孙组件。

   ```typescript
   @ComponentV2
   struct Son{
     build() {
       Column() {
         Grandson()
       }
     }
   }
   ```
3. 在孙子组件中使用@Consumer接收reviewVote参数。

   ```typescript
   @ComponentV2
   struct Grandson{
     @Consumer("reviewVote") reviewVotes: number = 0;

     build() {
       Column() {
         Button(`Grandson: ${this.reviewVotes}`)
       }.width('100%')
     }
   }
   ```

* 使用方式二：在父组件使用 @Local 装饰器，在子组件和孙子组件中使用 @Param 装饰器。

1. 在父组件Father中使用@Local绑定数据reviewVote。

   ```typescript
   @Entry
   @ComponentV2
   struct Father {
     @Local reviewVotes: number = 0;

     build() {
       Column() {
         Son({ reviewVotes: this.reviewVotes })
         Button(`Father: ${this.reviewVotes}`)
       }
     }
   }
   ```
2. 子组件Son中使用@Param接收父组件Father传递的参数reviewVote。

   ```typescript
   @ComponentV2
   struct Son {
     @Require @Param reviewVotes: number = 1;

     build() {
       Column() {
         Grandson({ reviewVotes: this.reviewVotes })
       }
     }
   }
   ```
3. 孙子组件Grandson 使用@Param接收Son组件传递的参数reviewVote。

   ```typescript
   @ComponentV2
   struct Grandson {
     @Require @Param reviewVotes: number = 1;

     build() {
       Column() {
         Button(`Grandson: ${this.reviewVotes}`)
       }.width('100%')
     }
   }
   ```
