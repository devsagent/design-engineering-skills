"use client";

import { useState } from "react";
import { ControlButton } from "./diagram-client";
import { ControlGroup, DiagramFrame } from "./diagram-primitives";
import styles from "./diagram.module.css";

const PHASES = ["intent", "durable", "apply", "terminal"] as const;
type Phase = (typeof PHASES)[number];
type Outcome = "receipt" | "retry";

type CausalFrame = {
  activeId: Phase | Outcome;
  completedIds: Array<Phase | Outcome>;
  readout: { label: string; value: string };
  implication: string;
  accessibleDescription: string;
  motionFrame: "idle" | "transfer" | "settled";
};

function deriveFrame(phaseIndex: number, outcome: Outcome): CausalFrame {
  const atTerminal = phaseIndex === PHASES.length - 1;
  const activeId = atTerminal ? outcome : PHASES[phaseIndex];
  const completedIds = PHASES.slice(0, phaseIndex);

  if (outcome === "retry" && atTerminal) {
    return {
      activeId,
      completedIds,
      readout: { label: "attempt", value: "1 of 2" },
      implication: "The request identity survives the timeout, so retrying does not duplicate the write.",
      accessibleDescription: "The request crossed the durability boundary and reached the worker. Storage timed out, so the worker routed the same request identity to the retry buffer instead of the receipt.",
      motionFrame: "settled",
    };
  }

  return {
    activeId,
    completedIds,
    readout: atTerminal
      ? { label: "total", value: "128 ms" }
      : { label: "phase", value: `${phaseIndex + 1} of ${PHASES.length}` },
    implication: atTerminal
      ? "A stored receipt makes later retries safe and observable."
      : "The same model drives node state, readout, detail copy, and accessibility text.",
    accessibleDescription: `The write is at ${PHASES[phaseIndex]}. ${phaseIndex} earlier phases are complete. The selected terminal outcome is ${outcome}.`,
    motionFrame: phaseIndex === 0 ? "idle" : "transfer",
  };
}

export function CausalFlowExample() {
  const [phaseIndex, setPhaseIndex] = useState(0);
  const [outcome, setOutcome] = useState<Outcome>("receipt");
  const frame = deriveFrame(phaseIndex, outcome);
  const nodes: Array<{ id: Phase | Outcome; label: string }> = [
    { id: "intent", label: "Intent" },
    { id: "durable", label: "Durable" },
    { id: "apply", label: "Apply" },
    { id: outcome, label: outcome === "receipt" ? "Receipt" : "Retry" },
  ];

  const controls = (
    <>
      <ControlGroup label="Sequence">
        <ControlButton
          onClick={() => setPhaseIndex((value) => Math.max(0, value - 1))}
          disabled={phaseIndex === 0}
        >
          Back
        </ControlButton>
        <ControlButton
          onClick={() => setPhaseIndex((value) => Math.min(PHASES.length - 1, value + 1))}
          disabled={phaseIndex === PHASES.length - 1}
        >
          Next
        </ControlButton>
        <ControlButton onClick={() => setPhaseIndex(0)}>Reset</ControlButton>
      </ControlGroup>
      <ControlGroup label="Terminal outcome">
        <ControlButton
          onClick={() => setOutcome("retry")}
          pressed={outcome === "retry"}
        >
          Storage timeout
        </ControlButton>
      </ControlGroup>
    </>
  );

  const details = (
    <div>
      <p className={styles.exampleReadout}>
        <span>{frame.readout.label}</span>
        <strong>{frame.readout.value}</strong>
      </p>
      <p>{frame.implication}</p>
      <code>motion: {frame.motionFrame}</code>
    </div>
  );

  return (
    <DiagramFrame
      anchorId="causal-flow-example"
      title="One model, every observable."
      description="Advance the write or introduce a storage timeout. Geometry, readout, implication, and accessible description derive from one frame."
      status={frame.implication}
      controls={controls}
      details={details}
      detailsLabel="Current causal frame"
    >
      <p id="causal-flow-description" className={styles.visuallyHidden}>
        {frame.accessibleDescription}
      </p>
      <div
        className={styles.exampleFlow}
        role="list"
        aria-describedby="causal-flow-description"
        data-motion={frame.motionFrame}
      >
        {nodes.map((node, index) => {
          const current = node.id === frame.activeId;
          const complete = frame.completedIds.includes(node.id);
          return (
            <div key={node.id} className={styles.exampleNodeWrap} role="listitem">
              <button
                type="button"
                className={styles.exampleNode}
                data-active={current ? "true" : undefined}
                data-complete={complete ? "true" : undefined}
                aria-current={current ? "step" : undefined}
                onClick={() => setPhaseIndex(index)}
              >
                <span>{String(index + 1).padStart(2, "0")}</span>
                <strong>{node.label}</strong>
              </button>
              {index < nodes.length - 1 ? (
                <span className={styles.exampleConnector} data-complete={complete ? "true" : undefined} aria-hidden="true" />
              ) : null}
            </div>
          );
        })}
      </div>
    </DiagramFrame>
  );
}
