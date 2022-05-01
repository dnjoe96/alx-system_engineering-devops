## Installing datdog for monitoring

## check information in datadog
curl -X GET "https://api.datadoghq.com/api/v1/hosts" -H "Content-Type: application/json" -H "DD-API-KEY: ${DD_API_KEY}" -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"


## get information on dashboard
curl -X GET "https://api.datadoghq.com/api/v1/dashboard" -H "Content-Type: application/json" -H "DD-API-KEY: ${DD_API_KEY}" -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
