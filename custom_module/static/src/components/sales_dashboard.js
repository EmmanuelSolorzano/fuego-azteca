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
        try {
            const response = await fetch('/fn1', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({file, calledBy}),
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
