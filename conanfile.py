from conan.tools.files import copy
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, cmake_layout
import os


class EBashRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    
    def requirements(self):
        # only actual requirement
        self.requires("doctest/2.4.11")

        # Check if a specific os or compiler
        #if self.settings.os != "Emscripten":
        #    self.requires("sdl/2.30.2")

    #def generate(self):
        # Used to copy additional files from a recipe into the build folder
    #    copy(self, "res/*", self.dependencies["imgui"].package_folder, os.path.join(self.build_folder, "imgui_src") )
    #    copy(self, "include/*", self.dependencies["imgui"].package_folder, os.path.join(self.build_folder, "imgui_src") )

