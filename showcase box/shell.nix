{ pkgs ? import <nixpkgs> {} }:

# Define the environment
pkgs.mkShell {
  buildInputs = with pkgs;[
    python312
    python312Packages.pip
    python312Packages.virtualenv
    python312Packages.numpy
    python312Packages.jupyter-core
    python312Packages.jupyter-console

    # vscode # PLUGINS: ms-python, jupyter notebooks, ocp-cad-viewer (https://github.com/bernhard-42/vscode-ocp-cad-viewer)
    vscodium-fhs

    # fix missing LibGL.so???
    python312Packages.pyopengl
    libGL
    libglvnd
  ];
  LD_LIBRARY_PATH = "${
      with pkgs;
      lib.makeLibraryPath [ stdenv.cc.cc.lib libGL xorg.libX11 xorg.libXi xorg.libXrender expat zlib ]
  }";

  # git clone https://github.com/Windfisch/eh21-b3d-workshop

  # pip install build123d ocp-vscode
  shellHook = "source .venv/bin/activate; codium --enable-proposed-api ms-toolsai.jupyter --enable-proposed-api ms-python design.py";
}
