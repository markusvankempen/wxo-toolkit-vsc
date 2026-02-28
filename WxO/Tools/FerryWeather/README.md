# FerryWeather Tool

OpenAPI tool for the FerryLight weather station API at https://nodered.ferrylight.online/rbweather.

## Data returned

- **Weather**: temp, humidity, wind, solar radiation, UV, rain
- **Tides**: tide data
- **Moon phases**: moonphases
- **Sunrise/sunset**: sunriseset
- **Air quality**: faqhi, diyaqhi
- **Weather alerts**: weatheralerts
- **Forecast**: weatherforecast
- **Soil moisture**: soilmoisture1/2/3, soilad, soilbatt

## Connection

Uses **basic authentication** (username/password). Credentials go in `.env_connection_<env>`:

```
CONN_FerryWeather_USERNAME=ferrylight
CONN_FerryWeather_PASSWORD=ferrylight
```

## Create and replicate

```bash
cd internal/WxO\ ImporterAndExport
./create_and_replicate_ferry_weather_tool.sh --source TZ1 --target TZ2
```

Or run as part of full test suite: `./run_wxo_tests.sh --full` (step 13: ferry_weather_replicate).
