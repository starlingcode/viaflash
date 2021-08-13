# Viatools

Viaflash extended to provide a GUI for the Python scripts used to generate Via resources. 

## Strategy

### Rewrite existing Viaflash functionality in Python using PySide.
- Needs error checking
- Needs local firmware flow
- Needs testing

### Sync3 Ratio Editor
- Select ratio set from Viaflash
- Button option to edit selected ratio set
- Formailze ratio set data structure
    - Scale set is a collection of scales
    - Scales are the fundamental data structure, consisting of a group of seed ratios and a tiling strategy
    - Scales are stored in the filesystem and downloaded from a repository
    - Scale sets are stored in a single json manifest with lists of scale name slugs and perhaps metadata
    - Scales are stored in another json manifest with each scale as an object referenced by a unique slug containing a set of seed ratios, a tiling strategy, and metadata
    - The state of the editor needs some kind of representation
- Implement front end for that data structure
- Incorporate binary generation from scale data in the editor and then flashing custom ratios in Viaflash
- Prepare reverse-compatible firmware version to be used in the repo
 
