# Blender Custom Properties Exporter
## [Download .zip](https://github.com/sjkillen/blender-export-custom-properties/releases/download/0.01/export-scene-custom-props-blender-addon.zip)
<a href='https://ko-fi.com/I2I57UQ7M' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://cdn.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>


Export objects' custom properties as a JSON file

## Example

![Cubert](./img/cubert.png)
![export location](./img/location.png)

```json
[
    {
        "type": "Scene",
        "name": "Scene",
        "data": [
            {
                "type": "Object",
                "name": "Cube",
                "data": [
                    [
                        "age",
                        "0.1"
                    ],
                    [
                        "name",
                        "Cubert"
                    ]
                ]
            }
        ]
    }
]
```

# Limitations
- Only exports things found in scene.objects
- Data is always converted to a string
- Pull request welcome :)
