export function get_attributes(res) {
    let attributes = res.attributes;
    $("#inv-attrs").append(
        `<div class="col">
            <hr>
            <div class="row">
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">STR:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-str" value=${attributes.STR[0] > 9 ? attributes.STR[0] : "0" + attributes.STR[0]}>
                        <input type="text" readonly class="form-control" id="inv-str" value=${attributes.STR[1] > 9 ? attributes.STR[2] : "0" + attributes.STR[1]}>
                        <input type="text" readonly class="form-control" id="inv-str" value=${attributes.STR[2] > 9 ? attributes.STR[1] : "0" + attributes.STR[2]}>
                    </div>
                </div>
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">DEX:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-dex" value=${attributes.DEX[0] > 9 ? attributes.DEX[0] : "0" + attributes.DEX[0]}>
                        <input type="text" readonly class="form-control" id="inv-dex" value=${attributes.DEX[1] > 9 ? attributes.DEX[2] : "0" + attributes.DEX[1]}>
                        <input type="text" readonly class="form-control" id="inv-dex" value=${attributes.DEX[2] > 9 ? attributes.DEX[1] : "0" + attributes.DEX[2]}>
                    </div>
                </div>
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">POW:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-pow" value=${attributes.POW[0] > 9 ? attributes.POW[0] : "0" + attributes.POW[0]}>
                        <input type="text" readonly class="form-control" id="inv-pow" value=${attributes.POW[1] > 9 ? attributes.POW[2] : "0" + attributes.POW[1]}>
                        <input type="text" readonly class="form-control" id="inv-pow" value=${attributes.POW[2] > 9 ? attributes.POW[1] : "0" + attributes.POW[2]}>
                    </div>
                </div>
            </div >
            <hr>
            <div class="row">
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">CON:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-con" value=${attributes.CON[0] > 9 ? attributes.CON[0] : "0" + attributes.CON[0]}>
                        <input type="text" readonly class="form-control" id="inv-con" value=${attributes.CON[1] > 9 ? attributes.CON[2] : "0" + attributes.CON[1]}>
                        <input type="text" readonly class="form-control" id="inv-con" value=${attributes.CON[2] > 9 ? attributes.CON[1] : "0" + attributes.CON[2]}>
                    </div>
                </div >
    
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">APP:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-app" value=${attributes.APP[0] > 9 ? attributes.APP[0] : "0" + attributes.APP[0]}>
                        <input type="text" readonly class="form-control" id="inv-app" value=${attributes.APP[1] > 9 ? attributes.APP[1] : "0" + attributes.APP[1]}>
                        <input type="text" readonly class="form-control" id="inv-app" value=${attributes.APP[2] > 9 ? attributes.APP[1] : "0" + attributes.APP[2]}>
                    </div>
                </div >

                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">EDU:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-edu" value=${attributes.EDU[0] > 9 ? attributes.EDU[0] : "0" + attributes.EDU[0]}>
                        <input type="text" readonly class="form-control" id="inv-edu" value=${attributes.EDU[1] > 9 ? attributes.EDU[2] : "0" + attributes.EDU[1]}>
                        <input type="text" readonly class="form-control" id="inv-edu" value=${attributes.EDU[2] > 9 ? attributes.EDU[1] : "0" + attributes.EDU[2]}>
                    </div>
                </div >
            </div>
            <hr>
            <div class="row">
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">SIZ:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-siz" value=${attributes.SIZ[0] > 9 ? attributes.SIZ[0] : "0" + attributes.SIZ[0]}>
                        <input type="text" readonly class="form-control" id="inv-siz" value=${attributes.SIZ[1] > 9 ? attributes.SIZ[2] : "0" + attributes.SIZ[1]}>
                        <input type="text" readonly class="form-control" id="inv-siz" value=${attributes.SIZ[2] > 9 ? attributes.SIZ[1] : "0" + attributes.SIZ[2]}>
                    </div>
                </div >
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">INT:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-int" value=${attributes.INT[0] > 9 ? attributes.INT[0] : "0" + attributes.INT[0]}>
                        <input type="text" readonly class="form-control" id="inv-int" value=${attributes.INT[1] > 9 ? attributes.INT[2] : "0" + attributes.INT[1]}>
                        <input type="text" readonly class="form-control" id="inv-int" value=${attributes.INT[2] > 9 ? attributes.INT[1] : "0" + attributes.INT[2]}>
                    </div>
                </div >
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">MOV:</span>
                        </div>
                        <input type="text" readonly class="form-control" id="inv-mov" value=${attributes.MOV}>
                    </div>
                </div>
            </div>
            <hr>
            <div class="row">
                <input type="submit" class="btn btn-danger" value="Update">
            </div>
        </div>`
    );
    $("#inv-extra-attr").append(
        `<div class="col">
            Build: <b>${attributes.BUILD[1]} </b>
        </div >
        <div class="col offset-md-7">
            Damage Bonus: <b>${attributes.BUILD[0]}</b>
        </div>`
    )
}


export function post_attributes(res) {
    let attributes = res.attributes;
    $("#inv-attrs").children().remove();
    $("#inv-extra-attr").children().remove();
    $("#inv-attrs").append(
        `<div class="col">
            <hr>
            <div class="row">
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">STR:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-str" value=${attributes.STR[0] > 9 ? attributes.STR[0] : "0" + attributes.STR[0]}>
                        <input type="text" readonly class="form-control" id="inv-str" value=${attributes.STR[1] > 9 ? attributes.STR[2] : "0" + attributes.STR[1]}>
                        <input type="text" readonly class="form-control" id="inv-str" value=${attributes.STR[2] > 9 ? attributes.STR[1] : "0" + attributes.STR[2]}>
                    </div>
                </div>
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">DEX:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-dex" value=${attributes.DEX[0] > 9 ? attributes.DEX[0] : "0" + attributes.DEX[0]}>
                        <input type="text" readonly class="form-control" id="inv-dex" value=${attributes.DEX[1] > 9 ? attributes.DEX[2] : "0" + attributes.DEX[1]}>
                        <input type="text" readonly class="form-control" id="inv-dex" value=${attributes.DEX[2] > 9 ? attributes.DEX[1] : "0" + attributes.DEX[2]}>
                    </div>
                </div>
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">POW:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-pow" value=${attributes.POW[0] > 9 ? attributes.POW[0] : "0" + attributes.POW[0]}>
                        <input type="text" readonly class="form-control" id="inv-pow" value=${attributes.POW[1] > 9 ? attributes.POW[2] : "0" + attributes.POW[1]}>
                        <input type="text" readonly class="form-control" id="inv-pow" value=${attributes.POW[2] > 9 ? attributes.POW[1] : "0" + attributes.POW[2]}>
                    </div>
                </div>
            </div >
            <hr>
            <div class="row">
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">CON:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-con" value=${attributes.CON[0] > 9 ? attributes.CON[0] : "0" + attributes.CON[0]}>
                        <input type="text" readonly class="form-control" id="inv-con" value=${attributes.CON[1] > 9 ? attributes.CON[2] : "0" + attributes.CON[1]}>
                        <input type="text" readonly class="form-control" id="inv-con" value=${attributes.CON[2] > 9 ? attributes.CON[1] : "0" + attributes.CON[2]}>
                    </div>
                </div >
    
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">APP:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-app" value=${attributes.APP[0] > 9 ? attributes.APP[0] : "0" + attributes.APP[0]}>
                        <input type="text" readonly class="form-control" id="inv-app" value=${attributes.APP[1] > 9 ? attributes.APP[1] : "0" + attributes.APP[1]}>
                        <input type="text" readonly class="form-control" id="inv-app" value=${attributes.APP[2] > 9 ? attributes.APP[1] : "0" + attributes.APP[2]}>
                    </div>
                </div >

                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">EDU:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-edu" value=${attributes.EDU[0] > 9 ? attributes.EDU[0] : "0" + attributes.EDU[0]}>
                        <input type="text" readonly class="form-control" id="inv-edu" value=${attributes.EDU[1] > 9 ? attributes.EDU[2] : "0" + attributes.EDU[1]}>
                        <input type="text" readonly class="form-control" id="inv-edu" value=${attributes.EDU[2] > 9 ? attributes.EDU[1] : "0" + attributes.EDU[2]}>
                    </div>
                </div >
            </div>
            <hr>
            <div class="row">
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">SIZ:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-siz" value=${attributes.SIZ[0] > 9 ? attributes.SIZ[0] : "0" + attributes.SIZ[0]}>
                        <input type="text" readonly class="form-control" id="inv-siz" value=${attributes.SIZ[1] > 9 ? attributes.SIZ[2] : "0" + attributes.SIZ[1]}>
                        <input type="text" readonly class="form-control" id="inv-siz" value=${attributes.SIZ[2] > 9 ? attributes.SIZ[1] : "0" + attributes.SIZ[2]}>
                    </div>
                </div >
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">INT:</span>
                        </div>
                        <input type="number" class="form-control" id="inv-int" value=${attributes.INT[0] > 9 ? attributes.INT[0] : "0" + attributes.INT[0]}>
                        <input type="text" readonly class="form-control" id="inv-int" value=${attributes.INT[1] > 9 ? attributes.INT[2] : "0" + attributes.INT[1]}>
                        <input type="text" readonly class="form-control" id="inv-int" value=${attributes.INT[2] > 9 ? attributes.INT[1] : "0" + attributes.INT[2]}>
                    </div>
                </div >
                <div class="col">
                    <div style="text-align: right" class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="">MOV:</span>
                        </div>
                        <input type="number" readonly class="form-control" id="inv-mov" value=${attributes.MOV}>
                    </div>
                </div>
            </div>
            <hr>
            <div class="row">
                <input type="submit" class="btn btn-danger" value="Update">
            </div>
            
        </div>`
    );
    $("#inv-extra-attr").append(
        `<div class="col">
            Build: <b>${attributes.BUILD[1]} </b>
        </div >
        <div class="col offset-md-7">
            Damage Bonus: <b>${attributes.BUILD[0]}</b>
        </div>`
    )
}