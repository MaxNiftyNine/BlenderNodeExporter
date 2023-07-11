# Blender Node Exporter
Exports Blender material nodes in a (Kinda) readable format

Just select your material, paste this script into blenders scripting tab and run!
The file should save into your user folder as exported_material_nodes.txt

Heres an example of what the script exports
```
Material: Spider-Verse
Node: TEX_COORD

Node: TEX_VORONOI
	Vector: Linked
	W: 0.0
	Scale: 100.0
	Smoothness: 1.0
	Exponent: 0.5
	Randomness: 0.0
	Connection: Mapping --> TEX_VORONOI --> Vector

Node: VALTORGB
	Fac: Linked
	Connection: Shader to RGB --> VALTORGB --> Color

Node: VALTORGB
	Fac: Linked
	Connection: Voronoi Texture.001 --> VALTORGB --> Distance

Node: MAPPING
	Vector: Linked
	Location: (0.0, 0.0, 0.0)
	Rotation: (0.0, 0.0, 0.0)
	Scale: (1.7000000476837158, 1.0, 1.0)
	Connection: Texture Coordinate --> MAPPING --> Window

Node: SHADERTORGB
	Shader: Linked
	Connection: Principled BSDF --> SHADERTORGB --> BSDF

Node: TEX_WAVE
	Vector: Linked
	Scale: 40.0
	Distortion: 0.10000000149011612
	Detail: 2.0
	Detail Scale: 1.0
	Detail Roughness: 0.5
	Phase Offset: 0.0
	Connection: Mapping --> TEX_WAVE --> Vector

Node: MIX
	Factor: 1.0
	Factor: 1.0
	A: 0.0
	B: 0.0
	A: 0.0
	B: 0.0
	A: 0.0
	B: 0.0
	Connection: ColorRamp.003 --> MIX --> Color
	Connection: ColorRamp.002 --> MIX --> Color

Node: VALTORGB
	Fac: Linked
	Connection: Wave Texture --> VALTORGB --> Color

Node: VALTORGB
	Fac: Linked
	Connection: Shader to RGB --> VALTORGB --> Color

Node: MIX
	Factor: 1.0
	Factor: 1.0
	A: 0.0
	B: 0.0
	A: 0.0
	B: 0.0
	A: 0.0
	B: 0.0
	Connection: ColorRamp --> MIX --> Color
	Connection: ColorRamp.001 --> MIX --> Color

Node: INVERT
	Fac: 1.0
	Color: Linked
	Connection: Mix.002 --> INVERT --> Result

Node: MIX
	Factor: 1.0
	Factor: 1.0
	A: 0.0
	B: 0.0
	A: 0.0
	B: 0.0
	A: 0.0
	B: 0.0
	Connection: Mix --> MIX --> Result
	Connection: Mix.001 --> MIX --> Result

Node: BSDF_PRINCIPLED
	Base Color: (0.800000011920929, 0.800000011920929, 0.800000011920929)
	Subsurface: 0.0
	Subsurface Radius: (1.0, 0.20000000298023224, 0.10000000149011612)
	Subsurface Color: (0.800000011920929, 0.800000011920929, 0.800000011920929)
	Subsurface IOR: 1.399999976158142
	Subsurface Anisotropy: 0.0
	Metallic: 0.0
	Specular: 0.5
	Specular Tint: 0.0
	Roughness: 0.5
	Anisotropic: 0.0
	Anisotropic Rotation: 0.0
	Sheen: 0.0
	Sheen Tint: 0.5
	Clearcoat: 0.0
	Clearcoat Roughness: 0.029999999329447746
	IOR: 1.4500000476837158
	Transmission: 0.0
	Transmission Roughness: 0.0
	Emission: (0.0, 0.0, 0.0)
	Emission Strength: 1.0
	Alpha: 1.0
	Normal: (0.0, 0.0, 0.0)
	Clearcoat Normal: (0.0, 0.0, 0.0)
	Tangent: (0.0, 0.0, 0.0)
	Weight: 0.0

Node: OUTPUT_MATERIAL
	Surface: Linked
	Volume: Not Applicable
	Displacement: (0.0, 0.0, 0.0)
	Thickness: 0.0
	Connection: Mix.003 --> OUTPUT_MATERIAL --> Result

Node: MIX
	Factor: 1.0
	Factor: 1.0
	A: 0.0
	B: 0.0
	A: 0.0
	B: 0.0
	A: 0.0
	B: 0.0
	Connection: Invert --> MIX --> Color
	Connection: Shader to RGB --> MIX --> Color

```
