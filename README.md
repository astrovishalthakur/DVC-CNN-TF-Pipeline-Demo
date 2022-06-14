# DVC-CNN-TF-Pipeline-Demo

<img src="others\docs\DVC-CNN-pipeline@2x (1).png" alt="workflow" width="70%">

DVL project for deep-learning usecase using tensor-flow

## STEPS

### STEP 01- Create a repository by using template repository.

### STEP 02- Clone the new repository.

### STEP 03- Create a conda environment after opening the repository in vscode.

```bash 
conda create --prefix ./env python=3.7 -y
```

```bash
conda activate ./env
```

OR

```bash
source activate ./env
```

### STEP 04- Install the requirements.
```bash
pip install -r requirements.txt
```

### STEP 05- Initialize the dvc project
```bash
dvc init
```

### STEP 06- Commit and push changes to remote repository.