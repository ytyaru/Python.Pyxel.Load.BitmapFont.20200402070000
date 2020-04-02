#!/bin/bash
Run() {
	ResourceDir() {
		local HERE="$(cd "$(dirname "$(realpath "${BASH_SOURCE:-0}")")"; pwd)"
		local PARENT="$(dirname "$HERE")"
		local RES="${PARENT}/res"
		echo "${RES}"
	}
	local RES="$(ResourceDir)"; mkdir -p "$RES";
	echo "$RES"
	local FILE='x8y12pxTheStrongGamer'
	local TTF="${FILE}.ttf"
	local PNG="${FILE}.png"
#	[ ! -f "$TTF" ] && wget http://www17.plala.or.jp/xxxxxxx/00ff/"$TTF"
#	[ ! -f "$PNG" ] && python3 BitmapFontGenerator.py
	echo "${RES}/${TTF}"
	[ ! -f "${RES}/${TTF}" ] && echo 'nai' || echo 'aru'
#	return
	[ ! -f "${RES}/${TTF}" ] && wget -O "${RES}/${TTF}" http://www17.plala.or.jp/xxxxxxx/00ff/"$TTF"
	[ ! -f "${RES}/${PNG}" ] && python3 BitmapFontGenerator.py
	python3 main.py
}
Run
