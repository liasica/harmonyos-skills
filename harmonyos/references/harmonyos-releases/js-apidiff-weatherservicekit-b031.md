---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-weatherservicekit-b031
title: Weather Service Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Weather Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:46+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:2056021dd371bef31b238e87368bbfa580874b177f8b8b710784b119363420cc
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace weatherService  差异内容： declare namespace weatherService | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明：function getWeather(request: WeatherRequest): Promise<Weather>;  差异内容：function getWeather(request: WeatherRequest): Promise<Weather>; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface WeatherRequest  差异内容： interface WeatherRequest | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherRequest；  API声明：location: Location;  差异内容：location: Location; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherRequest；  API声明：limitedDatasets?: Dataset[];  差异内容：limitedDatasets?: Dataset[]; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface Location  差异内容： interface Location | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Location；  API声明：latitude: number;  差异内容：latitude: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Location；  API声明：longitude: number;  差异内容：longitude: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface Weather  差异内容： interface Weather | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Weather；  API声明：current?: CurrentWeather;  差异内容：current?: CurrentWeather; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Weather；  API声明：daily?: Forecast<DailyWeather>;  差异内容：daily?: Forecast<DailyWeather>; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Weather；  API声明：hourly?: Forecast<HourlyWeather>;  差异内容：hourly?: Forecast<HourlyWeather>; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Weather；  API声明：minute?: Forecast<MinuteWeather>;  差异内容：minute?: Forecast<MinuteWeather>; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Weather；  API声明：alerts?: WeatherAlert[];  差异内容：alerts?: WeatherAlert[]; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Weather；  API声明：indices?: WeatherIndex[];  差异内容：indices?: WeatherIndex[]; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Weather；  API声明：tides?: Tide[];  差异内容：tides?: Tide[]; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Weather；  API声明：metadata: WeatherMetadata;  差异内容：metadata: WeatherMetadata; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Weather；  API声明：attributions: WeatherAttribution[];  差异内容：attributions: WeatherAttribution[]; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface WeatherMetadata  差异内容： interface WeatherMetadata | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherMetadata；  API声明：requestTime: Date;  差异内容：requestTime: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherMetadata；  API声明：version: string;  差异内容：version: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherMetadata；  API声明：timeZone?: string;  差异内容：timeZone?: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface WeatherAttribution  差异内容： interface WeatherAttribution | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAttribution；  API声明：serviceName: string;  差异内容：serviceName: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAttribution；  API声明：legalPageUrl: string;  差异内容：legalPageUrl: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface CurrentWeather  差异内容： interface CurrentWeather | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CurrentWeather；  API声明：temperature: number;  差异内容：temperature: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CurrentWeather；  API声明：apparentTemperature: number;  差异内容：apparentTemperature: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CurrentWeather；  API声明：humidity: number;  差异内容：humidity: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CurrentWeather；  API声明：pressure: number;  差异内容：pressure: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CurrentWeather；  API声明：pressureTrend: PressureTrend;  差异内容：pressureTrend: PressureTrend; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CurrentWeather；  API声明：wind: Wind;  差异内容：wind: Wind; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CurrentWeather；  API声明：cloudCover: number;  差异内容：cloudCover: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CurrentWeather；  API声明：condition: WeatherCondition;  差异内容：condition: WeatherCondition; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CurrentWeather；  API声明：uvIndex: UVIndex;  差异内容：uvIndex: UVIndex; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CurrentWeather；  API声明：aqi?: WeatherAqi;  差异内容：aqi?: WeatherAqi; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CurrentWeather；  API声明：visibility: number;  差异内容：visibility: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CurrentWeather；  API声明：updateTime: Date;  差异内容：updateTime: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CurrentWeather；  API声明：expirationTime: Date;  差异内容：expirationTime: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CurrentWeather；  API声明：summary?: string;  差异内容：summary?: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface WeatherCondition  差异内容： interface WeatherCondition | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherCondition；  API声明：type: ConditionType;  差异内容：type: ConditionType; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherCondition；  API声明：icon: resourceManager.Resource;  差异内容：icon: resourceManager.Resource; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherCondition；  API声明：description: string;  差异内容：description: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface Wind  差异内容： interface Wind | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Wind；  API声明：direction: CompassDirection;  差异内容：direction: CompassDirection; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Wind；  API声明：speed: number;  差异内容：speed: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Wind；  API声明：level: number;  差异内容：level: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Wind；  API声明：gustDirection?: CompassDirection;  差异内容：gustDirection?: CompassDirection; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Wind；  API声明：gustSpeed?: number;  差异内容：gustSpeed?: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Wind；  API声明：gustLevel?: number;  差异内容：gustLevel?: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface UVIndex  差异内容： interface UVIndex | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：UVIndex；  API声明：category: ExposureCategory;  差异内容：category: ExposureCategory; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：UVIndex；  API声明：value: number;  差异内容：value: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：UVIndex；  API声明：description: string;  差异内容：description: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface Forecast  差异内容： interface Forecast | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Forecast；  API声明：forecast: T[];  差异内容：forecast: T[]; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Forecast；  API声明：updateTime: Date;  差异内容：updateTime: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Forecast；  API声明：expirationTime: Date;  差异内容：expirationTime: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Forecast；  API声明：summary?: string;  差异内容：summary?: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface DailyWeather  差异内容： interface DailyWeather | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyWeather；  API声明：date: Date;  差异内容：date: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyWeather；  API声明：highTemperature: number;  差异内容：highTemperature: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyWeather；  API声明：lowTemperature: number;  差异内容：lowTemperature: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyWeather；  API声明：highApparentTemperature: number;  差异内容：highApparentTemperature: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyWeather；  API声明：lowApparentTemperature: number;  差异内容：lowApparentTemperature: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyWeather；  API声明：uvIndex: UVIndex;  差异内容：uvIndex: UVIndex; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyWeather；  API声明：aqi?: WeatherAqi;  差异内容：aqi?: WeatherAqi; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyWeather；  API声明：visibility: number;  差异内容：visibility: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyWeather；  API声明：moon: MoonEvents;  差异内容：moon: MoonEvents; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyWeather；  API声明：sun: SunEvents;  差异内容：sun: SunEvents; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyWeather；  API声明：daytimeForecast: DayPartForecast;  差异内容：daytimeForecast: DayPartForecast; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyWeather；  API声明：overnightForecast: DayPartForecast;  差异内容：overnightForecast: DayPartForecast; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyWeather；  API声明：pressure: number;  差异内容：pressure: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface SunEvents  差异内容： interface SunEvents | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：SunEvents；  API声明：sunrise: Date;  差异内容：sunrise: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：SunEvents；  API声明：sunset: Date;  差异内容：sunset: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface DayPartForecast  差异内容： interface DayPartForecast | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DayPartForecast；  API声明：wind: Wind;  差异内容：wind: Wind; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DayPartForecast；  API声明：humidity: number;  差异内容：humidity: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DayPartForecast；  API声明：cloudCover: number;  差异内容：cloudCover: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DayPartForecast；  API声明：condition: WeatherCondition;  差异内容：condition: WeatherCondition; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DayPartForecast；  API声明：precipitationProbability: number;  差异内容：precipitationProbability: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DayPartForecast；  API声明：precipitationAmount: number;  差异内容：precipitationAmount: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DayPartForecast；  API声明：rainfallProbability?: number;  差异内容：rainfallProbability?: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DayPartForecast；  API声明：rainfallAmount?: number;  差异内容：rainfallAmount?: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DayPartForecast；  API声明：snowfallProbability?: number;  差异内容：snowfallProbability?: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DayPartForecast；  API声明：snowfallAmount?: number;  差异内容：snowfallAmount?: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface MoonEvents  差异内容： interface MoonEvents | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonEvents；  API声明：moonrise: Date;  差异内容：moonrise: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonEvents；  API声明：moonset: Date;  差异内容：moonset: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonEvents；  API声明：phase: MoonPhase;  差异内容：phase: MoonPhase; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonEvents；  API声明：illuminatedFraction?: number;  差异内容：illuminatedFraction?: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonEvents；  API声明：age?: number;  差异内容：age?: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface MoonPhase  差异内容： interface MoonPhase | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonPhase；  API声明：type: MoonPhaseType;  差异内容：type: MoonPhaseType; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonPhase；  API声明：description: string;  差异内容：description: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonPhase；  API声明：icon: resourceManager.Resource;  差异内容：icon: resourceManager.Resource; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface HourlyWeather  差异内容： interface HourlyWeather | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyWeather；  API声明：date: Date;  差异内容：date: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyWeather；  API声明：temperature: number;  差异内容：temperature: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyWeather；  API声明：apparentTemperature: number;  差异内容：apparentTemperature: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyWeather；  API声明：humidity: number;  差异内容：humidity: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyWeather；  API声明：wind: Wind;  差异内容：wind: Wind; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyWeather；  API声明：cloudCover: number;  差异内容：cloudCover: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyWeather；  API声明：condition: WeatherCondition;  差异内容：condition: WeatherCondition; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyWeather；  API声明：uvIndex: UVIndex;  差异内容：uvIndex: UVIndex; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyWeather；  API声明：aqi?: WeatherAqi;  差异内容：aqi?: WeatherAqi; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyWeather；  API声明：visibility: number;  差异内容：visibility: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyWeather；  API声明：precipitationProbability: number;  差异内容：precipitationProbability: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyWeather；  API声明：precipitationAmount: number;  差异内容：precipitationAmount: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface MinuteWeather  差异内容： interface MinuteWeather | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MinuteWeather；  API声明：date: Date;  差异内容：date: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MinuteWeather；  API声明：precipitation: Precipitation;  差异内容：precipitation: Precipitation; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MinuteWeather；  API声明：precipitationIntensity: number;  差异内容：precipitationIntensity: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface WeatherAlert  差异内容： interface WeatherAlert | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAlert；  API声明：updateTime: Date;  差异内容：updateTime: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAlert；  API声明：expirationTime: Date;  差异内容：expirationTime: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAlert；  API声明：id: string;  差异内容：id: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAlert；  API声明：title: string;  差异内容：title: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAlert；  API声明：region?: string;  差异内容：region?: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAlert；  API声明：level: AlertLevel;  差异内容：level: AlertLevel; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAlert；  API声明：levelDescription: string;  差异内容：levelDescription: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAlert；  API声明：type: AlertType;  差异内容：type: AlertType; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAlert；  API声明：typeDescription: string;  差异内容：typeDescription: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAlert；  API声明：content: string;  差异内容：content: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAlert；  API声明：guide?: string;  差异内容：guide?: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAlert；  API声明：detailsUrl?: string;  差异内容：detailsUrl?: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAlert；  API声明：source: string;  差异内容：source: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAlert；  API声明：icon?: resourceManager.Resource;  差异内容：icon?: resourceManager.Resource; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface WeatherAqi  差异内容： interface WeatherAqi | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAqi；  API声明：no2?: number;  差异内容：no2?: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAqi；  API声明：o3?: number;  差异内容：o3?: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAqi；  API声明：pm10?: number;  差异内容：pm10?: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAqi；  API声明：pm25?: number;  差异内容：pm25?: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAqi；  API声明：so2?: number;  差异内容：so2?: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAqi；  API声明：co?: number;  差异内容：co?: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAqi；  API声明：aqiValue: number;  差异内容：aqiValue: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAqi；  API声明：aqiCategory: AqiCategory;  差异内容：aqiCategory: AqiCategory; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherAqi；  API声明：aqiDescription: string;  差异内容：aqiDescription: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface WeatherIndex  差异内容： interface WeatherIndex | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndex；  API声明：updateTime: Date;  差异内容：updateTime: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndex；  API声明：expirationTime: Date;  差异内容：expirationTime: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndex；  API声明：type: WeatherIndexType;  差异内容：type: WeatherIndexType; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndex；  API声明：name: string;  差异内容：name: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndex；  API声明：dailyItems: DailyIndex[];  差异内容：dailyItems: DailyIndex[]; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface DailyIndex  差异内容： interface DailyIndex | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyIndex；  API声明：date: Date;  差异内容：date: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyIndex；  API声明：level: number;  差异内容：level: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyIndex；  API声明：levelDescription: string;  差异内容：levelDescription: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：DailyIndex；  API声明：content: string;  差异内容：content: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface Tide  差异内容： interface Tide | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Tide；  API声明：updateTime: Date;  差异内容：updateTime: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Tide；  API声明：expirationTime: Date;  差异内容：expirationTime: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Tide；  API声明：stationId: string;  差异内容：stationId: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Tide；  API声明：stationName: string;  差异内容：stationName: string; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Tide；  API声明：hourlyTides: HourlyTide[];  差异内容：hourlyTides: HourlyTide[]; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： interface HourlyTide  差异内容： interface HourlyTide | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyTide；  API声明：date: Date;  差异内容：date: Date; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyTide；  API声明：category?: TideCategory;  差异内容：category?: TideCategory; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：HourlyTide；  API声明：height: number;  差异内容：height: number; | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： enum Dataset  差异内容： enum Dataset | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Dataset；  API声明：CURRENT = 0  差异内容：CURRENT = 0 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Dataset；  API声明：DAILY = 1  差异内容：DAILY = 1 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Dataset；  API声明：HOURLY = 2  差异内容：HOURLY = 2 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Dataset；  API声明：MINUTE = 3  差异内容：MINUTE = 3 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Dataset；  API声明：ALERTS = 4  差异内容：ALERTS = 4 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Dataset；  API声明：INDICES = 5  差异内容：INDICES = 5 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Dataset；  API声明：TIDES = 6  差异内容：TIDES = 6 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： enum PressureTrend  差异内容： enum PressureTrend | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：PressureTrend；  API声明：UNDEFINED = 0  差异内容：UNDEFINED = 0 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：PressureTrend；  API声明：FALLING = 1  差异内容：FALLING = 1 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：PressureTrend；  API声明：RISING = 2  差异内容：RISING = 2 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：PressureTrend；  API声明：STEADY = 3  差异内容：STEADY = 3 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： enum ConditionType  差异内容： enum ConditionType | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：UNDEFINED = 0  差异内容：UNDEFINED = 0 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：SUNNY = 1  差异内容：SUNNY = 1 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MOSTLY\_SUNNY = 2  差异内容：MOSTLY\_SUNNY = 2 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：PARTLY\_SUNNY = 3  差异内容：PARTLY\_SUNNY = 3 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：INTERMITTENT\_CLOUDS = 4  差异内容：INTERMITTENT\_CLOUDS = 4 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：HAZY\_SUNSHINE = 5  差异内容：HAZY\_SUNSHINE = 5 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MOSTLY\_CLOUDY = 6  差异内容：MOSTLY\_CLOUDY = 6 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：CLOUDY = 7  差异内容：CLOUDY = 7 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：OVERCAST = 8  差异内容：OVERCAST = 8 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：FOG = 11  差异内容：FOG = 11 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：SHOWERS = 12  差异内容：SHOWERS = 12 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MOSTLY\_CLOUDY\_WITH\_SHOWERS = 13  差异内容：MOSTLY\_CLOUDY\_WITH\_SHOWERS = 13 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：PARTLY\_SUNNY\_WITH\_SHOWERS = 14  差异内容：PARTLY\_SUNNY\_WITH\_SHOWERS = 14 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：T\_STORMS = 15  差异内容：T\_STORMS = 15 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MOSTLY\_CLOUDY\_WITH\_T\_STORMS = 16  差异内容：MOSTLY\_CLOUDY\_WITH\_T\_STORMS = 16 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：PARTLY\_SUNNY\_WITH\_T\_STORMS = 17  差异内容：PARTLY\_SUNNY\_WITH\_T\_STORMS = 17 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：RAIN = 18  差异内容：RAIN = 18 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：FLURRIES = 19  差异内容：FLURRIES = 19 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MOSTLY\_CLOUDY\_WITH\_FLURRIES = 20  差异内容：MOSTLY\_CLOUDY\_WITH\_FLURRIES = 20 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：PARTLY\_SUNNY\_WITH\_FLURRIES = 21  差异内容：PARTLY\_SUNNY\_WITH\_FLURRIES = 21 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：SNOW = 22  差异内容：SNOW = 22 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MOSTLY\_CLOUDY\_WITH\_SNOW = 23  差异内容：MOSTLY\_CLOUDY\_WITH\_SNOW = 23 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：ICE = 24  差异内容：ICE = 24 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：SLEET = 25  差异内容：SLEET = 25 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：FREEZING\_RAIN = 26  差异内容：FREEZING\_RAIN = 26 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：RAIN\_AND\_SNOW = 29  差异内容：RAIN\_AND\_SNOW = 29 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：HOT = 30  差异内容：HOT = 30 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：COLD = 31  差异内容：COLD = 31 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：WINDY = 32  差异内容：WINDY = 32 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：CLEAR = 33  差异内容：CLEAR = 33 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MOSTLY\_CLEAR = 34  差异内容：MOSTLY\_CLEAR = 34 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：PARTLY\_CLOUDY = 35  差异内容：PARTLY\_CLOUDY = 35 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：INTERMITTENT\_CLOUDS\_NIGHT = 36  差异内容：INTERMITTENT\_CLOUDS\_NIGHT = 36 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：HAZY\_MOONLIGHT = 37  差异内容：HAZY\_MOONLIGHT = 37 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MOSTLY\_CLOUDY\_NIGHT = 38  差异内容：MOSTLY\_CLOUDY\_NIGHT = 38 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：PARTLY\_CLOUDY\_WITH\_SHOWERS = 39  差异内容：PARTLY\_CLOUDY\_WITH\_SHOWERS = 39 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MOSTLY\_CLOUDY\_WITH\_SHOWERS\_NIGHT = 40  差异内容：MOSTLY\_CLOUDY\_WITH\_SHOWERS\_NIGHT = 40 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：PARTLY\_CLOUDY\_WITH\_T\_STORMS = 41  差异内容：PARTLY\_CLOUDY\_WITH\_T\_STORMS = 41 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MOSTLY\_CLOUDY\_WITH\_T\_STORMS\_NIGHT = 42  差异内容：MOSTLY\_CLOUDY\_WITH\_T\_STORMS\_NIGHT = 42 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MOSTLY\_CLOUDY\_WITH\_FLURRIES\_NIGHT = 43  差异内容：MOSTLY\_CLOUDY\_WITH\_FLURRIES\_NIGHT = 43 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MOSTLY\_CLOUDY\_WITH\_SNOW\_NIGHT = 44  差异内容：MOSTLY\_CLOUDY\_WITH\_SNOW\_NIGHT = 44 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：THUNDERSHOWER\_WITH\_HAIL = 45  差异内容：THUNDERSHOWER\_WITH\_HAIL = 45 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：LIGHT\_RAIN = 46  差异内容：LIGHT\_RAIN = 46 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MODERATE\_RAIN = 47  差异内容：MODERATE\_RAIN = 47 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：HEAVY\_RAIN = 48  差异内容：HEAVY\_RAIN = 48 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：STORM = 49  差异内容：STORM = 49 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：HEAVY\_STORM = 50  差异内容：HEAVY\_STORM = 50 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：SEVERE\_STORM = 51  差异内容：SEVERE\_STORM = 51 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：LIGHT\_SNOW = 52  差异内容：LIGHT\_SNOW = 52 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MODERATE\_SNOW = 53  差异内容：MODERATE\_SNOW = 53 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：HEAVY\_SNOW = 54  差异内容：HEAVY\_SNOW = 54 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：SNOWSTORM = 55  差异内容：SNOWSTORM = 55 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：DUST\_STORM = 56  差异内容：DUST\_STORM = 56 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：LIGHT\_TO\_MODERATE\_RAIN = 57  差异内容：LIGHT\_TO\_MODERATE\_RAIN = 57 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MODERATE\_TO\_HEAVY\_RAIN = 58  差异内容：MODERATE\_TO\_HEAVY\_RAIN = 58 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：HEAVY\_RAIN\_TO\_STORM = 59  差异内容：HEAVY\_RAIN\_TO\_STORM = 59 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：STORM\_TO\_HEAVY\_STORM = 60  差异内容：STORM\_TO\_HEAVY\_STORM = 60 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：HEAVY\_TO\_SEVERE\_STORM = 61  差异内容：HEAVY\_TO\_SEVERE\_STORM = 61 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：LIGHT\_TO\_MODERATE\_SNOW = 62  差异内容：LIGHT\_TO\_MODERATE\_SNOW = 62 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MODERATE\_TO\_HEAVY\_SNOW = 63  差异内容：MODERATE\_TO\_HEAVY\_SNOW = 63 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：HEAVY\_SNOW\_TO\_SNOWSTORM = 64  差异内容：HEAVY\_SNOW\_TO\_SNOWSTORM = 64 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：DUST = 65  差异内容：DUST = 65 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：SAND = 66  差异内容：SAND = 66 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：SANDSTORM = 67  差异内容：SANDSTORM = 67 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：DENSE\_FOGGY = 68  差异内容：DENSE\_FOGGY = 68 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MODERATE\_FOGGY = 69  差异内容：MODERATE\_FOGGY = 69 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：MODERATE\_HAZE = 70  差异内容：MODERATE\_HAZE = 70 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：HEAVY\_HAZE = 71  差异内容：HEAVY\_HAZE = 71 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：SEVERE\_HAZE = 72  差异内容：SEVERE\_HAZE = 72 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：HEAVY\_FOGGY = 73  差异内容：HEAVY\_FOGGY = 73 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：SEVERE\_FOGGY = 74  差异内容：SEVERE\_FOGGY = 74 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：OVERCAST\_NIGHT = 75  差异内容：OVERCAST\_NIGHT = 75 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ConditionType；  API声明：BLOWING\_SNOW = 76  差异内容：BLOWING\_SNOW = 76 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： enum ExposureCategory  差异内容： enum ExposureCategory | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ExposureCategory；  API声明：UNDEFINED = 0  差异内容：UNDEFINED = 0 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ExposureCategory；  API声明：VERY\_LOW = 1  差异内容：VERY\_LOW = 1 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ExposureCategory；  API声明：LOW = 2  差异内容：LOW = 2 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ExposureCategory；  API声明：MODERATE = 3  差异内容：MODERATE = 3 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ExposureCategory；  API声明：HIGH = 4  差异内容：HIGH = 4 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：ExposureCategory；  API声明：VERY\_HIGH = 5  差异内容：VERY\_HIGH = 5 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： enum CompassDirection  差异内容： enum CompassDirection | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CompassDirection；  API声明：UNDEFINED = 0  差异内容：UNDEFINED = 0 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CompassDirection；  API声明：NORTH = 1  差异内容：NORTH = 1 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CompassDirection；  API声明：NORTH\_EAST = 2  差异内容：NORTH\_EAST = 2 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CompassDirection；  API声明：EAST = 3  差异内容：EAST = 3 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CompassDirection；  API声明：SOUTH\_EAST = 4  差异内容：SOUTH\_EAST = 4 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CompassDirection；  API声明：SOUTH = 5  差异内容：SOUTH = 5 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CompassDirection；  API声明：SOUTH\_WEST = 6  差异内容：SOUTH\_WEST = 6 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CompassDirection；  API声明：WEST = 7  差异内容：WEST = 7 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：CompassDirection；  API声明：NORTH\_WEST = 8  差异内容：NORTH\_WEST = 8 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： enum AlertType  差异内容： enum AlertType | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：TYPHOON = 1  差异内容：TYPHOON = 1 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：RAIN\_STORM = 2  差异内容：RAIN\_STORM = 2 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：SNOW\_STORM = 3  差异内容：SNOW\_STORM = 3 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：COLD\_WAVE = 4  差异内容：COLD\_WAVE = 4 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：GALE = 5  差异内容：GALE = 5 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：SAND\_STORM = 6  差异内容：SAND\_STORM = 6 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：HEAT\_WAVE = 7  差异内容：HEAT\_WAVE = 7 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：DROUGHT = 8  差异内容：DROUGHT = 8 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：LIGHTNING = 9  差异内容：LIGHTNING = 9 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：HAIL = 10  差异内容：HAIL = 10 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：FROST = 11  差异内容：FROST = 11 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：HEAVY\_FOG = 12  差异内容：HEAVY\_FOG = 12 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：HAZE = 13  差异内容：HAZE = 13 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：ROAD\_ICING = 14  差异内容：ROAD\_ICING = 14 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：OTHER = 15  差异内容：OTHER = 15 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：THUNDER\_AND\_GALE = 17  差异内容：THUNDER\_AND\_GALE = 17 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：FOREST\_FIRE\_RISK = 18  差异内容：FOREST\_FIRE\_RISK = 18 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：COLD = 19  差异内容：COLD = 19 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：DUST\_HAZE = 20  差异内容：DUST\_HAZE = 20 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：COOLING = 21  差异内容：COOLING = 21 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：ROAD\_ICE\_AND\_SNOW = 22  差异内容：ROAD\_ICE\_AND\_SNOW = 22 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：DRY\_HOT\_WIND = 23  差异内容：DRY\_HOT\_WIND = 23 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：HAZE\_VERY\_UNHEALTHY = 24  差异内容：HAZE\_VERY\_UNHEALTHY = 24 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：FROZEN = 25  差异内容：FROZEN = 25 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：HEAVY\_FOG\_AT\_SEA = 26  差异内容：HEAVY\_FOG\_AT\_SEA = 26 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：THUNDERSTORM\_AND\_GALE = 27  差异内容：THUNDERSTORM\_AND\_GALE = 27 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：CONTINUOUS\_LOW\_TEMPERATURE = 28  差异内容：CONTINUOUS\_LOW\_TEMPERATURE = 28 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：THICK\_DUST = 29  差异内容：THICK\_DUST = 29 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：TORNADO = 30  差异内容：TORNADO = 30 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：LOW\_TEMPERATURE\_FREEZE\_INJURY = 31  差异内容：LOW\_TEMPERATURE\_FREEZE\_INJURY = 31 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：GALE\_AT\_SEA = 32  差异内容：GALE\_AT\_SEA = 32 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：LOW\_TEMPERATURE\_FREEZING\_RAIN\_AND\_SNOW = 33  差异内容：LOW\_TEMPERATURE\_FREEZING\_RAIN\_AND\_SNOW = 33 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：SEVERE\_CONVECTION = 34  差异内容：SEVERE\_CONVECTION = 34 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：OZONE = 35  差异内容：OZONE = 35 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：HEAVY\_SNOW = 36  差异内容：HEAVY\_SNOW = 36 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：HEAVY\_RAINFALL = 37  差异内容：HEAVY\_RAINFALL = 37 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：STRONG\_COOLING = 38  差异内容：STRONG\_COOLING = 38 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：SNOW\_DISASTER = 39  差异内容：SNOW\_DISASTER = 39 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：FOREST\_GRASSLAND\_FIRE\_RISK = 40  差异内容：FOREST\_GRASSLAND\_FIRE\_RISK = 40 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：THUNDERSTORM = 41  差异内容：THUNDERSTORM = 41 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：SEVERE\_COLD = 42  差异内容：SEVERE\_COLD = 42 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：SAND\_DUST = 43  差异内容：SAND\_DUST = 43 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：THUNDERSTORM\_AND\_GALE\_AT\_SEA = 44  差异内容：THUNDERSTORM\_AND\_GALE\_AT\_SEA = 44 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：LIGHTNING\_AT\_SEA = 45  差异内容：LIGHTNING\_AT\_SEA = 45 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：TYPHOON\_AT\_SEA = 46  差异内容：TYPHOON\_AT\_SEA = 46 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：LOW\_TEMPERATURE = 47  差异内容：LOW\_TEMPERATURE = 47 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：GEOLOGICAL\_HAZARD = 48  差异内容：GEOLOGICAL\_HAZARD = 48 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：GEOLOGICAL\_HAZARD\_AND\_METEOROLOGICAL\_RISK = 49  差异内容：GEOLOGICAL\_HAZARD\_AND\_METEOROLOGICAL\_RISK = 49 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：FLUSH\_FLOOD = 50  差异内容：FLUSH\_FLOOD = 50 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：GRASSLAND\_FIRE\_RISK = 51  差异内容：GRASSLAND\_FIRE\_RISK = 51 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertType；  API声明：THUNDER\_RAIN\_AND\_GALE = 52  差异内容：THUNDER\_RAIN\_AND\_GALE = 52 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： enum AlertLevel  差异内容： enum AlertLevel | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertLevel；  API声明：BLUE = 1  差异内容：BLUE = 1 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertLevel；  API声明：YELLOW = 2  差异内容：YELLOW = 2 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertLevel；  API声明：ORANGE = 3  差异内容：ORANGE = 3 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertLevel；  API声明：RED = 4  差异内容：RED = 4 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertLevel；  API声明：OTHER = 5  差异内容：OTHER = 5 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertLevel；  API声明：WHITE = 6  差异内容：WHITE = 6 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AlertLevel；  API声明：BLACK = 7  差异内容：BLACK = 7 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： enum MoonPhaseType  差异内容： enum MoonPhaseType | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonPhaseType；  API声明：UNDEFINED = 0  差异内容：UNDEFINED = 0 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonPhaseType；  API声明：NEW = 1  差异内容：NEW = 1 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonPhaseType；  API声明：WAXING\_CRESCENT = 2  差异内容：WAXING\_CRESCENT = 2 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonPhaseType；  API声明：FIRST\_QUARTER = 3  差异内容：FIRST\_QUARTER = 3 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonPhaseType；  API声明：WAXING\_GIBBOUS = 4  差异内容：WAXING\_GIBBOUS = 4 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonPhaseType；  API声明：FULL = 5  差异内容：FULL = 5 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonPhaseType；  API声明：WANING\_GIBBOUS = 6  差异内容：WANING\_GIBBOUS = 6 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonPhaseType；  API声明：LAST\_QUARTER = 7  差异内容：LAST\_QUARTER = 7 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：MoonPhaseType；  API声明：WANING\_CRESCENT = 8  差异内容：WANING\_CRESCENT = 8 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： enum Precipitation  差异内容： enum Precipitation | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Precipitation；  API声明：NONE = 0  差异内容：NONE = 0 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Precipitation；  API声明：HAIL = 1  差异内容：HAIL = 1 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Precipitation；  API声明：RAIN = 2  差异内容：RAIN = 2 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Precipitation；  API声明：SLEET = 3  差异内容：SLEET = 3 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：Precipitation；  API声明：SNOW = 4  差异内容：SNOW = 4 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： enum AqiCategory  差异内容： enum AqiCategory | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AqiCategory；  API声明：UNDEFINED = 0  差异内容：UNDEFINED = 0 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AqiCategory；  API声明：EXCELLENT = 1  差异内容：EXCELLENT = 1 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AqiCategory；  API声明：GOOD = 2  差异内容：GOOD = 2 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AqiCategory；  API声明：SLIGHT = 3  差异内容：SLIGHT = 3 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AqiCategory；  API声明：MODERATE = 4  差异内容：MODERATE = 4 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AqiCategory；  API声明：HEAVY = 5  差异内容：HEAVY = 5 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：AqiCategory；  API声明：SEVERE = 6  差异内容：SEVERE = 6 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： enum WeatherIndexType  差异内容： enum WeatherIndexType | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndexType；  API声明：UNDEFINED = 0  差异内容：UNDEFINED = 0 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndexType；  API声明：DRESSING = 1  差异内容：DRESSING = 1 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndexType；  API声明：MOTION = 2  差异内容：MOTION = 2 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndexType；  API声明：COLD = 3  差异内容：COLD = 3 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndexType；  API声明：CAR\_WASHING = 4  差异内容：CAR\_WASHING = 4 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndexType；  API声明：TOURISM = 5  差异内容：TOURISM = 5 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndexType；  API声明：SUN\_PROTECTION = 7  差异内容：SUN\_PROTECTION = 7 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndexType；  API声明：FISHING = 8  差异内容：FISHING = 8 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndexType；  API声明：MORNING\_EXERCISE = 10  差异内容：MORNING\_EXERCISE = 10 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndexType；  API声明：ALLERGY = 24  差异内容：ALLERGY = 24 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndexType；  API声明：SKIING = 31  差异内容：SKIING = 31 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：WeatherIndexType；  API声明：STARGAZING = 34  差异内容：STARGAZING = 34 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：weatherService；  API声明： enum TideCategory  差异内容： enum TideCategory | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：TideCategory；  API声明：UNDEFINED = 0  差异内容：UNDEFINED = 0 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：TideCategory；  API声明：HIGH = 1  差异内容：HIGH = 1 | api/@hms.core.weather.d.ts |
| 新增API | NA | 类名：TideCategory；  API声明：LOW = 2  差异内容：LOW = 2 | api/@hms.core.weather.d.ts |
