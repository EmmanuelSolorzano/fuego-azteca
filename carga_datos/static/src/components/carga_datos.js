/** @odoo-module */

import { registry } from "@web/core/registry";

const { Component, useRef } = owl;

export class OwlCargaDatos extends Component {

    setup(){
        this.dropArea = useRef('Drag1');
    }

    handleAmazonFile(ev) {
        this.handleFileUpload(ev.target.files[0], 'c_amazon');
    }

    handleClientesFile(ev) {
        this.handleFileUpload(ev.target.files[0], 'c_clientes');
    }

    handleInventarioFile(ev) {
        this.handleFileUpload(ev.target.files[0], 'c_inventario');
    }

    async handleFileUpload(file, calledBy) {
        console.log('File:', file);
        // Create a promise that resolves with the file content
        const fileContentPromise = new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = (e) => resolve(e.target.result);
            reader.onerror = (e) => reject(new Error('Failed to read file'));
            reader.readAsText(file);
        });
    
        try {
            // Wait for the file to be read
            const text = await fileContentPromise;
            console.log('File Content:', text);
    
            const response = await fetch('/fn1', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({file: text, calledBy}),
            });
            // Handle the response here
            const data = await response.json();
            console.log('Data:', data.result);
            if (data.result !== 'Archivo procesado exitosamente!') {
                throw new Error('Failed to upload file');
            }

            if (data.result === 'Archivo procesado exitosamente!') {
                this.showSucessModal('Success', 'File uploaded successfully');
            }
        }
        catch (error) {
            console.error('Error:', error);
            this.showErrorModal();
        }
    }
    
    showSucessModal() {
        // Create a new div element
        const modalDiv = document.createElement('div');
        modalDiv.innerHTML = `
        <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" data-dismiss="modal">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title" id="myModalLabel">Carga exitosa!</h4>
              </div>
              <div class="modal-body">
                El archivo se ha cargado exitosamente!
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">Cerrar</button>
              </div>
            </div>
          </div>
        </div>
        `;
    
        // Append the new div element to the body
        document.body.appendChild(modalDiv);
        
    
        // Show the modal
        $('#myModal').modal('show');
        $('#myModal').on('shown.bs.modal', function () {
            $('.close').click(function () {
                $('#myModal').modal('hide');
            });
            $('.btn-default').click(function () {
                $('#myModal').modal('hide');
            });
        });
    }

    showErrorModal() {
            // Create a new div element
            const modalErrorDiv = document.createElement('div');
            modalErrorDiv.innerHTML = `
            <div class="modal fade" id="myErrorModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" data-dismiss="modal">
              <div class="modal-dialog" role="document">
                <div class="modal-content">
                  <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title" id="myModalLabel">Error</h4>
                  </div>
                  <div class="modal-body">
                    Ocurrió un error al cargar el archivo:
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Cerrar</button>
                  </div>
                </div>
              </div>
            </div>
            `;
        
            // Append the new div element to the body
            document.body.appendChild(modalErrorDiv);
        
            // Show the modal
            $('#myErrorModal').modal('show');
            $('#myErrorModal').on('shown.bs.modal', function () {
                $('.close').click(function () {
                    $('#myErrorModal').modal('hide');
                });
                $('.btn-default').click(function () {
                    $('#myErrorModal').modal('hide');
                });
            });
    }
}

OwlCargaDatos.template = "owl.OwlCargaDatos";
registry.category("actions").add("owl.carga_datos", OwlCargaDatos);
