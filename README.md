# ba-skader

## Overview

This README provides the necessary information to set up, configure, and use the microservice. It includes details about environmental variables, API endpoints, and dependencies.

The service can be accesed here: https://ba-skader-euanhqfffdage0as.northeurope-01.azurewebsites.net/apidocs


---

## Environmental Variables

The microservice requires the following environmental variables to be configured before running. Ensure these variables are set correctly in your environment.

| Variable  | Required | Default | Description                |
| --------- | -------- | ------- | -------------------------- |
| `DB_PATH` | Yes      | None    | Path to the database file. |

---

## API Endpoints

Below is a list of the API endpoints exposed by this microservice. Each endpoint includes the HTTP method, a brief description, possible status codes, and the returned data.

### Endpoints

| Path             | Method | Description                          | Status Codes   | Response                                                                                     |
|------------------|--------|--------------------------------------|----------------|---------------------------------------------------------------------------------------------|
| `/skader`        | GET   | Retrieve a list of all damages | 200, 404       | Array of objects each containing `skade_id`, `skade_type`, `skade_pris`, `nummerplade`, `syn_type` and `indberetnings_dato` or error message explaining failure.|
| `/skader`        | POST    | Create a new damage         | 201, 400       | Object with `skade_id`, `skade_type`, `skade_pris`, `nummerplade`, `syn_type` and `indberetnings_dato` or error message explaining failure.|


---

## Dependencies

The following dependencies are required to run the microservice. These are specified in the `requirements.txt` file.

---
