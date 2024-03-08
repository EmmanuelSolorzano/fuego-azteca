/** @odoo-module */

const { onWillStart, Component } = owl
import { loadJS } from "@web/core/assets"

export class KpiCard extends Component {
    setup() {
        onWillStart(async ()=>{
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js")
            const response = await fetch('/fn2', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ "data" : "kpi"}),
            });
            // Handle the response here
            const data = await response.json();
            var objData = JSON.parse(data.result || "{}");
            console.log(objData);
            this.value = objData[this.props.param] || 0;
            if (this.value % 1 !== 0) {
                this.value = parseFloat(this.value).toFixed(2);
            }
        })
        this.name = this.props.name;
        this.spa = this.props.spa;
    }
}

KpiCard.template = "owl.KpiCard";
KpiCard.props = {
    name: String,
    value: { type: Number, optional: true },
};
