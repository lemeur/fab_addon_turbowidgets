# Example Schema for APScheduler

## Generated form preview
<img src="images/json_editor_dependencies.gif" width="400">

## Corresponding schema

```
    scheduler_schema = {
        "type": "object",
        "title": " ",
        "required": ["mode","timezone"],
        "properties": {
            "mode": {
                "type": "string",
                "default": "interval",
                "propertyOrder": 1,
                "enum": [
                    "cron",
                    "interval",
                    "date"
                ]
            },
            "timezone": {
                "type": "string",
                "propertyOrder": 2,
                "default": "Europe/Paris",
                "options": {
                    "inputAttributes": {
                        "placeholder":  "Europe/Paris",
                    }
                }
            },
            "weeks": {
                "type": "integer",
                "propertyOrder": 10,
                "default": 0,
                "options": {
                    "dependencies": {
                        "mode": "interval"
                    }
                }
            },
            "days": {
                "type": "integer",
                "propertyOrder": 11,
                "default": 1,
                "options": {
                    "dependencies": {
                        "mode": "interval"
                    }
                }
            },
            "minutes": {
                "type": "integer",
                "propertyOrder": 12,
                "default": 0,
                "options": {
                    "dependencies": {
                        "mode": "interval"
                    }
                }
            },
            "seconds": {
                "type": "integer",
                "propertyOrder": 13,
                "default": 0,
                "options": {
                    "dependencies": {
                        "mode": "interval"
                    }
                }
            },
            "year": {
                "type": "string",
                "propertyOrder": 20,
                "default": "*",
                "options": {
                    "dependencies": {
                        "mode": "cron"
                    }
                }
            },
            "month": {
                "type": "string",
                "propertyOrder": 21,
                "default": "*",
                "options": {
                    "dependencies": {
                        "mode": "cron"
                    }
                }
            },
            "day": {
                "type": "string",
                "propertyOrder": 22,
                "default": "*",
                "options": {
                    "dependencies": {
                        "mode": "cron"
                    }
                }
            },
            "week": {
                "type": "string",
                "propertyOrder": 23,
                "default": "*",
                "options": {
                    "dependencies": {
                        "mode": "cron"
                    }
                }
            },
            "day_of_week": {
                "type": "string",
                "propertyOrder": 24,
                "default": "*",
                "options": {
                    "dependencies": {
                        "mode": "cron"
                    }
                }
            },
            "hour": {
                "type": "string",
                "propertyOrder": 25,
                "default": "*",
                "options": {
                    "dependencies": {
                        "mode": "cron"
                    }
                }
            },
            "minute": {
                "type": "string",
                "propertyOrder": 26,
                "default": "*",
                "options": {
                    "dependencies": {
                        "mode": "cron"
                    }
                }
            },
            "second": {
                "type": "string",
                "propertyOrder": 27,
                "default": "*",
                "options": {
                    "dependencies": {
                        "mode": "cron"
                    }
                }
            },
            "start_date": {
                "type": "string",
                "propertyOrder": 3,
                "default": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "format": "datetime",
                "options": {
                    "dependencies": {
                        "mode": ["interval","cron"]
                    },
                    "inputAttributes": {
                        "class":  "date",
                    }
                }
            },
            "end_date": {
                "type": "string",
                "propertyOrder": 4,
                "default": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "format": "datetime",
                "options": {
                    "dependencies": {
                        "mode": ["interval","cron"]
                    },
                    "inputAttributes": {
                        "class":  "date",
                    }
                }
            },
            "run_date": {
                "type": "string",
                "propertyOrder": 30,
                "default": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "format": "datetime",
                "options": {
                    "dependencies": {
                        "mode": "date"
                    }
                }
            }
        },
        "defaultProperties": ["mode","weeks","days","minutes","seconds","start_date","end_date","year","month","day","week","day_of_week","hour","minute","second","timezone","date"]
    }
```
