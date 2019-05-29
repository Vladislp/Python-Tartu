import cx_Freeze

executables = [cx_Freeze.Executable("kodu0.py")]

cx_Freeze.setup(
    name="Diary",
    options={"build_exe":{"packages":["pygame","Sys"],"include_files":["back.jpg","Cafe.jpg","car.jpg","dad.jpg","front.jpg","kitchen,jpg","liv.jpg","morning.jpg","room.jpg","street.jpg","work.jpg"]}},
    
    description = "Diary",
    executables = executables
    )