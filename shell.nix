# shell.nix, used in combination with nix develop
{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell rec {
  nativeBuildInputs = with pkgs; [
    libsForQt5.wrapQtAppsHook
    (python39.withPackages (ps: [ps.twine ps.wheel]))
    makeWrapper
  ];
  # https://discourse.nixos.org/t/python-qt-woes/11808/10
  shellHook = ''
    setQtEnvironment=$(mktemp --suffix .setQtEnvironment.sh)
    echo "shellHook: setQtEnvironment = $setQtEnvironment"
    makeWrapper "/bin/sh" "$setQtEnvironment" "''${qtWrapperArgs[@]}"
    sed "/^exec/d" -i "$setQtEnvironment"
    source "$setQtEnvironment"
  '';
}
