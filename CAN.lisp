;; Define the procedure to handle the event ID and data
(define proc-eid 
  (lambda (id data)
    (print (list id data)))) ; Print the ID and data

;; Define the event handler
(define event-handler 
  (lambda ()
    (progn
      ;; Receive the event and call the proc-eid function with the ID and data
      (recv ((signal-can-eid (? id) (? data)) 
             (proc-eid id data)) 
            (nil)) ; Ignore other events
      ;; Call self again to make this a loop
      (event-handler))))

;; Spawn the event handler thread and pass the ID it returns to C
(event-register-handler (spawn event-handler))

;; Enable the CAN event for standard ID SID frames
(event-enable "event-can-eid")
