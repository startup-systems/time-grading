# Grading script

The score is out of 100.


## Grading all submissions

_This is intended for staff._

1. Download the [class survey data](https://docs.google.com/spreadsheets/d/1aQkPiTDqfxBtZDBCWAkU7Sizlf_KLoMEzJkbwhXBgjo/edit#gid=209566137).
    * `File`->`Download as`->`Comma-separated values`
    * This file is used to map GitHub usernames to Cornell NetIDs.
1. From this directory, run:

    ```bash
    python run_all.py <path/to/responses>.csv grades.csv
    ```

1. `grades.csv` can then be uploaded to CMS.
    * `Assignments`->`Grade`->(assignment)->`Upload grades file`
