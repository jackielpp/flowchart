```mermaid
flowchart TD
    A[Start] --> B[Enter Username]
    B --> C[Enter Password]
    C --> H{Is password empty?}
    H -- Yes --> I[Show 'Password required' error]
    I --> C
    H -- No --> P{Is password in supported language?}
    P -- No --> Q[Show 'Unsupported language' error]
    Q --> C
    P -- Yes --> J{Network error?}
    J -- Yes --> K[Show 'Network error' message]
    K --> U[Increment retry count]
    U --> V{Retry count >= 3?}
    V -- Yes --> W[Show 'Please contact support' and End]
    V -- No --> C
    J -- No --> D{Is password correct?}
    D -- Yes --> R{Has password expired (older than 6 months)?}
    D -- No --> L[Increment failed attempts]
    L --> M{Failed attempts >= 3?}
    M -- Yes --> N[Lock account]
    N --> B
    M -- No --> F[Show 'Incorrect password' error]
    F --> C
    R -- Yes --> S[Prompt user to change password]
    S --> T{Password changed successfully?}
    T -- Yes --> E[Login successful]
    T -- No --> X[Show 'Please contact support' and End]
    R -- No --> E[Login successful]
    E --> G[End]
```
