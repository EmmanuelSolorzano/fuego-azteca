/** @odoo-module */

import { registry } from "@web/core/registry";
const { Component, useRef } = owl;

export class OwlSalesDashboard extends Component {

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
            console.log(data);
        }
        catch (error) {
            console.error('Error:', error);
            // Handle errors here
        }
    }
}

OwlSalesDashboard.template = "owl.OwlSalesDashboard";
registry.category("actions").add("owl.sales_dashboard", OwlSalesDashboard);
