# Pxl

> An image pixelator.

## Installation

You need to install the dependencies for the script. You can do that by running the following command.

```
pip install -r requirements.txt
```

*Note:* Run as `sudo` if that fails (common on MacOS).

## Usage

```
python pxl.py <square size> <color options> <method> <file>
```

| Argument | Description |
| ------------- |:-------------|
| square size | The size of the pixels after pixelation |
| color options | For method 0, the number of band colors to limit to. |
| method | One of the [available methods](#methods) |

### Methods

| Method | Description |
| ------------- |:-------------|
| 0 | Limit the number of possible band (R,G,B) values to a specific number. |
| 1 | Get a color from from an existing palette based on euclidean distance between the actual color and the palette colors. |
