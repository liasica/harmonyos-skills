---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-v1-state-object-member-used-in-fun-parameter
title: "@correctness/v1-state-object-member-used-in-function-parameter-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/v1-state-object-member-used-in-function-parameter-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d78400aec90e4e69a47e2056a5b9a67c8cb3b9096e2ce8c1f08577873a75aeb4
---

在 build() 方法内，避免将@Observed和@ObjectLink装饰的类对象的状态变量直接作为参数传递给方法（如 a.b(this.object)）。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@correctness/v1-state-object-member-used-in-function-parameter-check": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Observed
class Weather {
  temperature:number;

  constructor(temperature:number) {
    this.temperature = temperature;
  }

  static increaseTemperature(weather:Weather) {
    weather.temperature++;
  }
}

class Day {
  weather:Weather;
  week:string;
  constructor(weather:Weather, week:string) {
    this.weather = weather;
    this.week = week;
  }
}

@Entry
@Component
struct Parent {
  @State day1: Day = new Day(new Weather(15), 'Monday');

  build() {
    Column({ space:10 }) {
      Child({ weather: this.day1.weather})
    }
    .height('100%')
    .width('100%')
  }
}

@Component
struct Child {
  @ObjectLink weather: Weather;

  reduceTemperature (weather:Weather) {
    weather.temperature--;
  }

  build() {
    Column({ space:10 }) {
      Text(`The temperature of day1 is ${this.weather.temperature} degrees.`)
        .fontSize(20)
      Button('increaseTemperature')
        .onClick(()=>{
          // 通过赋值添加 Proxy 代理
          let weather1 = this.weather;
          Weather.increaseTemperature(weather1);
        })
      Button('reduceTemperature')
        .onClick(()=>{
          // 通过赋值添加 Proxy 代理
          let weather2 = this.weather;
          this.reduceTemperature(weather2);
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## 反例

```screen
@Observed
class Weather {
  temperature:number;

  constructor(temperature:number) {
    this.temperature = temperature;
  }

  static increaseTemperature(weather:Weather) {
    weather.temperature++;
  }
}

class Day {
  weather:Weather;
  week:string;
  constructor(weather:Weather, week:string) {
    this.weather = weather;
    this.week = week;
  }
}

@Entry
@Component
struct Parent {
  @State day1: Day = new Day(new Weather(15), 'Monday');

  build() {
    Column({ space:10 }) {
      Child({ weather: this.day1.weather})
    }
    .height('100%')
    .width('100%')
  }
}

@Component
struct Child {
  @ObjectLink weather: Weather;

  reduceTemperature (weather:Weather) {
    weather.temperature--;
  }

  build() {
    Column({ space:10 }) {
      Text(`The temperature of day1 is ${this.weather.temperature} degrees.`)
        .fontSize(20)
      Button('increaseTemperature')
        .onClick(()=>{
          // 通过静态方法调用，无法触发UI刷新
          Weather.increaseTemperature(this.weather);
        })
      Button('reduceTemperature')
        .onClick(()=>{
          // 使用this通过自定义组件内部方法调用，无法触发UI刷新
          this.reduceTemperature(this.weather);
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## 规则集

```screen
plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
