import neko
import platform

if platform.system() == "Windows":
    if not neko.is_installed("gdown"):
        neko.run_pip("install gdown", "requirements for Batchlinks Download extension")

    if not neko.is_installed("wget"):
        neko.run_pip("install wget", "requirements for Batchlinks Download extension")