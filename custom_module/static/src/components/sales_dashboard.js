/** @odoo-module */

import { registry } from "@web/core/registry";
const { Component, useRef } = owl;

export class OwlSalesDashboard extends Component {

    setup(){
        this.dropArea = useRef('Drag1');
    }

    fn1

    async baseCall(calledBy){
        const file = "Prueba de archivo";

        try {
            const response = await fetch('/fn1', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ file, calledBy }),
            });

            if (!response.ok) {
                throw new Error(`Error en la solicitud: ${response.statusText}`);
            }

            const resultado = await response.json();
            console.log('Respuesta del servidor:', resultado);


        } catch (error) {
            console.error('Error en la solicitud AJAX:', error);
        }
    }

    async c_amazon(){
        console.log("Amazon clickeado");
        const calledBy = 'c_amazon';
        this.baseCall(calledBy);
    }
    
    async c_clientes(){
        console.log("Clientes clickeado");
        const calledBy = 'c_clientes';
        this.baseCall(calledBy);

    }

    async c_inventario(){
        console.log("Inventario clickeado");
        const calledBy = 'c_inventario';
        this.baseCall(calledBy);
    }
}

OwlSalesDashboard.template = "owl.OwlSalesDashboard";
registry.category("actions").add("owl.sales_dashboard", OwlSalesDashboard);
